matrix: list = []
with open("input.txt", "r") as file:
    for line in file:
        matrix.append(list(line.strip()))

rows: int = len(matrix)
cols: int = len(matrix[0])

rolls: set = set()
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "@":
            rolls.add((i, j))

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
while True:
    occupied: list = []

    for i, j in rolls:
        count: int = 0

        for x, y in directions:
            temp_i: int = i + x
            temp_j: int = j + y

            if 0 <= temp_i < rows and 0 <= temp_j < cols:
                if (temp_i, temp_j) in rolls:
                    count += 1

            if count >= 4:
                break

        if count < 4:
            result += 1
            occupied.append((i, j))

    if not occupied:
        break

    for i, j in occupied:
        rolls.remove((i, j))

print(result)
