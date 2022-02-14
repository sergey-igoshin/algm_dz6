import sys


def numerical_series(num, s=0):
    if num == 1:
        print(f'Память {s}')
        return num
    s += sys.getsizeof(num)
    return num + numerical_series(num - 1, s)


def numerical_series2(num):
    if num == 1:
        return num
    return num + numerical_series2(num - 1)


num = 10
print(numerical_series(num))

# тоже самое
print(f'Память {sys.getsizeof(numerical_series2(num)) * (num - 1)}')
print(numerical_series2(num))
