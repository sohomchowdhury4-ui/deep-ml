def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	return[[element*scalar for element in raw] for raw in matrix]

matrix =[[1,2],
         [3,4]]
print(scalar_multiply(matrix, 2))