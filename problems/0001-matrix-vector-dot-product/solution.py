import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]):
	M =np.array(a)
	v =np.array(b)
	if M.shape[1] != v.shape[0]:
		return -1
	return M @ v
	