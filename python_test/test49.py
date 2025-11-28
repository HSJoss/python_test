
import torch as th
import numpy as np

import numbers


class Transform:
    def transform(self, tensor):
        raise NotImplementedError

    def infer_output_info(self, vshape_in, dtype_in):
        raise NotImplementedError


class OneHot(Transform):
    def __init__(self, out_dim):
        self.out_dim = out_dim

    def transform(self, tensor):
        y_onehot = tensor.new(*tensor.shape[:-1], self.out_dim).zero_()
        y_onehot.scatter_(-1, tensor.long(), 1)
        return y_onehot.float()

    def infer_output_info(self, vshape_in, dtype_in):
        return (self.out_dim,), th.float32


scheme = {
    "state": {"vshape": (80,), "dtype": th.float32},
    "obs": {"vshape": {"image":(3,84,84), "position":10}, "group": "agents", "dtype": th.float32},
    "actions": {"vshape": {"a":(1,), "n":(1,)}, "group": "agents", "dtype": th.long},
    "avail_actions": {"vshape": (4,), "group": "agents", "dtype": th.int},
    "reward": {"vshape": (1,), "episode_const":True},
    "terminated": {"vshape": (1,), "dtype": th.uint8},
}
groups = {
    "agents": 5
}
preprocess = {
    "actions": ("actions_onehot", [OneHot(out_dim=4)])
}




def apply_transforms_recursive(vshape, dtype, transforms):
    if isinstance(vshape, dict):
        return {
            k: apply_transforms_recursive(vshape[k], dtype, transforms)
            for k in vshape
        }
    else:
        for transform in transforms:
            vshape, dtype = transform.infer_output_info(vshape, dtype)
        return vshape, dtype
    
for k in preprocess:
    assert k in scheme
    new_k = preprocess[k][0]
    transforms = preprocess[k][1]

    vshape = scheme[k]["vshape"]
    dtype = scheme[k]["dtype"]

    if isinstance(vshape, dict):
        transformed = {
            kk: apply_transforms_recursive(vv, dtype, transforms)
            for kk, vv in vshape.items()
        }
        vshape = {kk: v for kk, (v, _) in transformed.items()}
        dtype_set = {d for _, (_, d) in transformed.items()}
        dtype = dtype_set.pop()
    else:
        vshape, dtype = apply_transforms_recursive(vshape, dtype, transforms)

    scheme[new_k] = {
        "vshape": vshape,
        "dtype": dtype
    }
    if "group" in scheme[k]:
        scheme[new_k]["group"] = scheme[k]["group"]


assert "filled" not in scheme, '"filled" is a reserved key for masking.'
scheme.update({
    "filled": {"vshape": (1,), "dtype": th.long},
})






















batch_size = 100 # 버퍼 크기
max_seq_length = 200 # 게임 길이


transition_data = {}
episode_data = {}
def normalize_vshape(vshape):
    if isinstance(vshape, dict):
        return {k: normalize_vshape(v) for k, v in vshape.items()}
    elif isinstance(vshape, numbers.Integral):
        return (vshape,)
    else:
        return vshape

def make_tensor_recursive(vshape, dtype, shape_prefix, device):
    if isinstance(vshape, dict):
        return {
            k: make_tensor_recursive(sub_vshape, dtype, shape_prefix, device)
            for k, sub_vshape in vshape.items()
        }
    else:
        #return th.zeros((*shape_prefix, *vshape), dtype=dtype, device=device).shape
        return th.zeros((*shape_prefix, *vshape), dtype=dtype, device=device)

for field_key, field_info in scheme.items():
    assert "vshape" in field_info, f"Scheme must define vshape for {field_key}"
    vshape = normalize_vshape(field_info["vshape"])
    field_info["vshape"] = vshape
    episode_const = field_info.get("episode_const", False)
    group = field_info.get("group", None)
    dtype = field_info.get("dtype", th.float32)

    # shape prefix 구성
    shape_prefix = [batch_size]
    if not episode_const:
        shape_prefix.append(max_seq_length)
    if group:
        assert group in groups, f"Group {group} must have its number of members defined in groups"
        shape_prefix.append(groups[group])

    # 재귀적으로 텐서 생성
    tensor = make_tensor_recursive(vshape, dtype, shape_prefix, "cpu")

    # 저장
    if episode_const:
        episode_data[field_key] = tensor
    else:
        transition_data[field_key] = tensor


def recursive_transform(orig_tensor, transforms):
    if isinstance(orig_tensor, dict):
        return {
            subk: recursive_transform(orig_tensor[subk], transforms)
            for subk in orig_tensor
        }
    else:
        for transform in transforms:
            orig_tensor = transform.transform(orig_tensor)
        return orig_tensor






























def update(data, bs=slice(None), ts=slice(None), mark_filled=True):
    slices = _parse_slices((bs, ts))

    for k, v in data.items():
        if k in transition_data:
            target = transition_data
            if mark_filled:
                target["filled"][slices] = 1
                mark_filled = False
            _slices = slices
        elif k in episode_data:
            target = episode_data
            _slices = slices[0]
        else:
            raise KeyError(f"{k} not found in transition or episode data")

        dtype = scheme[k].get("dtype", th.float32)
        recursive_update(target, k, v, _slices, dtype)

        if k in preprocess:
            new_k = preprocess[k][0]
            transforms = preprocess[k][1]
            transformed = recursive_transform(target[k][_slices], transforms)
            recursive_assign(target, new_k, transformed, _slices)

def recursive_update(target, key, value, slices, dtype):
    if isinstance(value[0], dict):
        for subkey in value[0]:
            recursive_update(target[key], subkey, value[0][subkey], slices, dtype)
    else:
        #print(value)
        v = th.tensor(value, dtype=dtype, device="cpu")
        _check_safe_view(v, target[key][slices])
        target[key][slices] = v.view_as(target[key][slices])

def recursive_transform(tensor, transforms):
    if isinstance(tensor, dict):
        return {
            k: recursive_transform(tensor[k], transforms)
            for k in tensor
        }
    else:
        for transform in transforms:
            tensor = transform.transform(tensor)
        return tensor

def recursive_assign(target, key, value, slices):
    if isinstance(value, dict):
        for subkey in value:
            recursive_assign(target[key], subkey, value[subkey], slices)
    else:
        _check_safe_view(value, target[key][slices])
        target[key][slices] = value.view_as(target[key][slices])

def _check_safe_view(v, dest):
        #print(dest.shape)
        idx = len(v.shape) - 1
        for s in dest.shape[::-1]:
            if v.shape[idx] != s:
                if s != 1:
                    raise ValueError(f"Unsafe reshape of {v.shape} to {dest.shape}")
            else:
                idx -= 1

def _parse_slices(items):
        parsed = []
        # Only batch slice given, add full time slice
        if (isinstance(items, slice)  # slice a:b
            or isinstance(items, int)  # int i
            or (isinstance(items, (list, np.ndarray, th.LongTensor, th.cuda.LongTensor)))  # [a,b,c]
            ):
            items = (items, slice(None))

        # Need the time indexing to be contiguous
        if isinstance(items[1], list):
            raise IndexError("Indexing across Time must be contiguous")

        for item in items:
            #TODO: stronger checks to ensure only supported options get through
            if isinstance(item, int):
                # Convert single indices to slices
                parsed.append(slice(item, item+1))
            else:
                # Leave slices and lists as is
                parsed.append(item)
        return parsed

test_data = {
    "obs": [],
}

input_data = {"image":th.ones((1, 1, 5, *scheme["obs"]["vshape"]["image"]), dtype=scheme["obs"]["dtype"], device="cpu"),
              "position":th.ones((1, 1, 5, *scheme["obs"]["vshape"]["position"]), dtype=scheme["obs"]["dtype"], device="cpu")
}

test_data["obs"].append(input_data)


update(test_data, 1, 1)



print(scheme)
#print(episode_data)
#print(transition_data)
print(transition_data["obs"]["image"][1,1,:])
print(transition_data["obs"]["position"][1,1,:])

