count = 0
ranges = []
ingredients = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        if not line:
            continue

        parts: list[str] = line.split("-")
        if len(parts) == 2:
            low = int(parts[0])
            high = int(parts[1])

            ranges.append((low, high))
        elif len(parts) == 1:
            ingredients.append(int(parts[0]))

for ingredient in ingredients:
    for low, high in ranges:
        if low <= ingredient <= high:
            count += 1
            break

print(count)
