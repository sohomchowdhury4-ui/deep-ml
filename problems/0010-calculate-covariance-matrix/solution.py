def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n = len(vectors)
    means =[]
    for vector in vectors:
        mean = sum(vector)/len(vector)
        means.append(mean)
    convariance_matrix =[]
    for i in range(n):
        row =[]
        for j in range(n):
            convariance = 0
            for k in range(len(vectors[i])):
                convariance += (vectors[i][k] - means[i])*(vectors[j][k] - means[j])
            convariance = convariance/(len(vectors[i]) - 1)
            row.append(convariance)
        convariance_matrix.append(row)
    return convariance_matrix
vectors =[[1, 2, 3], [4, 5, 6]]
print(calculate_covariance_matrix(vectors))

