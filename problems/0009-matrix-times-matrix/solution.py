def matrixmul(A: list, B: list) -> list[list[int | float]]:
    if len(A[0]) != len(B):
        return -1
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            total = 0
            for k in range(len(B)):
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)
    return result
    
A=[[1,2],
   [2,4]]
B=[[2,1],
   [3,4]]
print(matrixmul(A, B))
