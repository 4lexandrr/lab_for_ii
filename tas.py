import numpy as np


def solution(array_a, array_b):
    array_a = np.array(array_a)
    array_b = np.array(array_b)
    print(np.sum(abs(array_b - array_a)))
    res = np.sum(abs(array_b - array_a) ** 2) / len(array_a)
    return res


a1 = [1,2,3]
a2 = [4,5,6]
print(solution(a1, a2))