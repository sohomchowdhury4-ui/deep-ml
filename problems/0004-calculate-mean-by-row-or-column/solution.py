def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix:
        return []

    if mode == "row":
        return [sum(row) / len(row) for row in matrix]

    elif mode == "column":
        rows = len(matrix)
        cols = len(matrix[0])
        return [
            sum(matrix[i][j] for i in range(rows)) / rows
            for j in range(cols)
        ]

    else:
        return []