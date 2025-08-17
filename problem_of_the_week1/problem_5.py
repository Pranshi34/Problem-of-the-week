def word_in_matrix(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        row_str = "".join(matrix[r])
        if word in row_str:
            return True

    for c in range(cols):
        col_str = "".join(matrix[r][c] for r in range(rows))
        if word in col_str:
            return True

    return False


m, n = map(int, input().split())

matrix = []
for _ in range(m):
    row = input().split()
    matrix.append(row)

word = input().strip()

print(word_in_matrix(matrix, word))
