from gymnasium import Env, spaces, utils
import numpy as np

observation_space1 = spaces.Discrete(16)
obs_shape1 = observation_space1.shape
obs_n1 = observation_space1.n

observation_space2 = spaces.Box(
    low=0.0,
    high=3.0,  # 최대값은 채널 2 기준으로 (H = 3)
    shape=(2, 4, 4),
    dtype=np.uint8
)
obs_shape2 = observation_space2.shape
#obs_n2 = observation_space2.n

observation_space3 = spaces.Box(
    low=-1.0,
    high=1.0,
    shape=(10,),
    dtype=np.float32
)
obs_shape3 = observation_space3.shape
#obs_n3 = observation_space3.n

print(type(observation_space1))
print(type(observation_space2))
print(type(observation_space3))
print(obs_shape1)
print(obs_shape2)
print(obs_shape3)
print(obs_n1)
#print(obs_n2)
#print(obs_n3)

def is_single_tuple(obj):
    return isinstance(obj, tuple) and all(not isinstance(x, tuple) for x in obj)

def is_tuple_of_tuples(obj):
    return isinstance(obj, tuple) and all(isinstance(x, tuple) for x in obj)


def a():
    return (3, 84, 84), (3,)

k = a()

print(type(k))
print(k[1])


x = ((3, 84, 84), (3,))
y = (3, 84, 84)

print(is_tuple_of_tuples(x))  # True
print(is_tuple_of_tuples(y))  # False
print(is_single_tuple(x))     # False
print(is_single_tuple(y))     # True
