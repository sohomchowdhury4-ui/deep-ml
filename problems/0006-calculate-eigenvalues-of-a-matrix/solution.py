import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a, b = matrix[0][0], matrix[0][1]
	c, d = matrix[1][0], matrix[1][1]
	trace = a + d 
	det = a*d - b*c
	lamda1 =(trace + math.sqrt(trace**2-4*det))/2
	lamda2 =(trace - math.sqrt(trace**2-4*det))/2
	return sorted([lamda1, lamda2], reverse=True)

matrix =[[2,1],
		 [1,2]]
print(calculate_eigenvalues(matrix))