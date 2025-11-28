import torch as th


# dummy_inputs = []
# for vshape in input_vshapes:
#     dummy_inputs.append(th.zeros(self.args.batch_size*self.n_agents, vshape[0] * vshape[1], *vshape[2:]) if len(vshape) == 4 else th.zeros(self.args.batch_size*self.n_agents, *vshape))
# dummy_input = th.cat(dummy_inputs, dim=1)

v = (16,16)
a = th.zeros(3, *v)

print(a.shape)



result_shape = (3,5,5) + (7,)
print(result_shape)