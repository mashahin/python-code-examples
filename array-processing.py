# array functions
import numpy as np
from numpy import zeros


def array_product(input_arr):
    """
    compute product of array elements except self

    """
    n = len(input_arr)
    out_arr = np.array(zeros(n, dtype=int))
    for i in range(n):
        product = 1
        for j in range(n):
            if (i != j):
                product *= input_arr[j]
        out_arr[i] = product
    return out_arr


def array_sum_of_products(input_arr):
    """
    compute sum of products of array element pairs
    input array of n integer elements reduces to n-1 elements 

    """
    n = len(input_arr)
    out_arr = np.array(zeros(n-1), dtype=int)
    for i in range(n-1):
        sum = 0
        for j in range(i+1, n):
            sum += input_arr[i]*input_arr[j]
        out_arr[i] = sum
    return out_arr


# array elements can take on zero, +ve, or -ve integer values
# a = np.array([0, 1, 2, 3, 4], dtype=int)
# a = np.array([], dtype=int)
a = np.array([1, -2, 3, 4], dtype=int)
print(f"input array: {a}")
print(f"products array: {array_product(a)}")
print(f"sum of products: {array_sum_of_products(a)}")
print(f"array inverted: {a[::-1]}")
