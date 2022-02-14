import os
from decor import time_size
from random import sample


@time_size
def func(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


nums = [i for i in sample(range(0, 100000000), 100000)]

r, m, t = func(nums)
print(os.path.basename(__file__))
print(f'{m} MiB', f'{t} sec', sep='\n')
