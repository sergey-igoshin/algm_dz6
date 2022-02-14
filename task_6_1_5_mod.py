import os
from decor import time_size
from random import sample


@time_size
def func(nums):
    return (i for i in range(len(nums)) if not nums[i] % 2)


nums = [i for i in sample(range(0, 100000000), 100000)]

r, m, t = func(nums)
print(os.path.basename(__file__))
print(f'{m} MiB', f'{t} sec', sep='\n')

