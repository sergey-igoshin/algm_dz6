from memory_profiler import memory_usage
import time


def time_size(func):
    def wrapper(*args, **kwargs):
        mem_1 = memory_usage()
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        mem_2 = memory_usage()
        time_diff = end_time - start_time
        mem_diff = mem_2[0] - mem_1[0]
        return res, mem_diff, time_diff
    return wrapper
