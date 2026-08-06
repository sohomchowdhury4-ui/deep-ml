import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    a = np.array(A)
    t = np.array(T)
    s = np.array(S)
    if np.linalg.det(t) == 0 or np.linalg.det(s) == 0:
        return -1
    invers_t = np.linalg.inv(t)
    result= invers_t@a@s
    return result.tolist()

A = [[1, 2],
     [3, 4]]
T = [[2, 0], 
     [0, 2]]
S = [[1, 1], 
     [0, 1]]
print(transform_matrix(A, T, S))