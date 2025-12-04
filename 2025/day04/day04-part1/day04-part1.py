matrix: list = []
with open("input.txt", "r") as file:
    for line in file:
        matrix.append(list(line.strip()))

rows: int = len(matrix)
cols: int = len(matrix[0])

directions: list = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

result: int = 0
for i in range(rows):
    for j in range(cols):
        current: int = matrix[i][j]
        count: int = 0

        if current == ".":
            continue

        for x, y in directions:
            temp_i: int = i + x
            temp_j: int = j + y

            if 0 <= temp_i < rows and 0 <= temp_j < cols:
                if matrix[temp_i][temp_j] == "@":
                    count += 1

            if count >= 4:
                break

        if count < 4:
            result += 1

print(result)
