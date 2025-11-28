import cv2
import numpy as np
from typing import Tuple

def resize_image_tensor(
    image: np.ndarray,
    shape: Tuple[int, int] = (84, 84),
    interpolation=cv2.INTER_AREA
) -> np.ndarray:
    """
    Resize an image or stack of images with shape [C, H, W] or [S, C, H, W] to (H, W) = shape.
    """
    # 단일 이미지인지 stack인지 확인
    if image.ndim == 3:  # [C, H, W]
        C, H, W = image.shape
        resized = _resize_single(image, shape, interpolation)
        return resized
    elif image.ndim == 4:  # [S, C, H, W]
        S, C, H, W = image.shape
        resized_stack = np.stack(
            [_resize_single(image[i], shape, interpolation) for i in range(S)],
            axis=0
        )
        return resized_stack
    else:
        raise ValueError(f"Unsupported image shape: {image.shape}")

def _resize_single(image: np.ndarray, shape: Tuple[int, int], interpolation) -> np.ndarray:
    """
    Resize a single image with shape [C, H, W] to [C, H_out, W_out].
    """
    C, H, W = image.shape
    resized_channels = [
        cv2.resize(image[c], shape, interpolation=interpolation) for c in range(C)
    ]
    resized = np.stack(resized_channels, axis=0)  # [C, H_out, W_out]
    return resized


img = np.random.randint(0, 256, (3, 120, 160), dtype=np.uint8)  # [C, H, W]
resized_img = resize_image_tensor(img, shape=(84, 84))

img_stack = np.random.randint(0, 256, (4, 3, 100, 100), dtype=np.uint8)  # [S, C, H, W]
resized_stack = resize_image_tensor(img_stack, shape=(84, 84))

print(resized_img.shape)
print(resized_stack.shape)