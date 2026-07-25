
# def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
# 	#Write your code here and return a python list after reshaping by using numpy's tolist() method
# 	return reshaped_matrix
import numpy as np
def reshape_matrix(a, b):
	try:
         return np.reshape(a,b).tolist()
	except ValueError:
         return []


a = np.array([[1,2,3,4],[5,6,7,8]])
b =(4, 2)
print(reshape_matrix(a, b))
