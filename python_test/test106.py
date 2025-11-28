import math
import numpy as np
from typing import List, Optional
#from .my_frozen_lake import generate_random_map  # 경로 맞게 수정 필요

def make_map_pool(
    num_maps: int,
    size: int = 8,
    poisson: bool = True,
    p_min: float = 0.6,
    p_max: float = 0.8,
    use_fixed_p: bool = False,
    seed: Optional[int] = None,
) -> List[List[str]]:
    """
    Generate a list of valid maps for FrozenLake using variable sizes and probabilities.

    Parameters
    ----------
    num_maps : int
        Number of maps to generate.
    size : int
        Used as the mean for Poisson distribution (if enabled).
    poisson : bool
        Whether to use Poisson distribution to sample sizes.
    p_min, p_max : float
        Range for uniform sampling of p values.
    use_fixed_p : bool
        If True, use (p_min + p_max) / 2 instead of random sampling.
    seed : int, optional
        Base seed for reproducibility (must ensure unique seeds per map).

    Returns
    -------
    maps : List[List[str]]
        A list of map descriptions (each a list of strings).
    """
    if num_maps == 1:
        poisson = False
        use_fixed_p = True

    rng = np.random.default_rng(seed)

    # 1. Map sizes
    sizes = []
    while len(sizes) < num_maps:
        if poisson:
            s = rng.poisson(size)
            prob = math.exp(-size) * size**s / math.factorial(s)
            if prob < 0.0001 or s < 4:
                continue  # 너무 드문 경우나 너무 작은 맵 제외
            sizes.append(s)
        else:
            sizes.append(size)

    # 2. Map probabilities
    if use_fixed_p:
        p_vals = [round((p_min + p_max) / 2, 4)] * num_maps
    else:
        p_vals = rng.uniform(low=p_min, high=p_max, size=num_maps).round(4).tolist()

    # 3. Unique seed per map
    map_seeds = rng.integers(0, 1e9, size=num_maps)

    # 4. Generate maps
    maps = []
    for s, p, map_seed in zip(sizes, p_vals, map_seeds):
        #desc = generate_random_map(size=s, p=p, seed=int(map_seed))
        desc = [s, p, int(map_seed)]
        maps.append(desc)

    return maps


maps = make_map_pool(
    num_maps=10,
    seed=42
)

print(maps)
