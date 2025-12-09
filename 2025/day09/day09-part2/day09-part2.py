from shapely.geometry import Polygon, box

tiles: list[tuple] = []  # (col, row)
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        col, row = line.split(",")
        tiles.append((int(col), int(row)))

poly = Polygon(tiles)
num_tiles = len(tiles)

result = 0
for i in range(0, num_tiles):
    for j in range(i + 1, num_tiles):
        t1 = tiles[i]
        t2 = tiles[j]

        min_x = min(t1[0], t2[0])
        max_x = max(t1[0], t2[0])
        min_y = min(t1[1], t2[1])
        max_y = max(t1[1], t2[1])

        width = max_x - min_x + 1
        height = max_y - min_y + 1
        area = width * height

        if area <= result:
            continue

        candidate = box(min_x, min_y, max_x, max_y)

        if poly.covers(candidate):
            result = area

print(result)
