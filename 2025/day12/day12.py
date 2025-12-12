with open("input.txt", "r") as file:
    content = file.read()
    parts = content.split("\n\n")
    presents = parts[:-1]
    regions = parts[-1].splitlines()

    sizes: dict[int, int] = {}
    for present in presents:
        lines = present.splitlines()
        index = int(lines[0][:-1])
        size = 0
        for line in lines[1:]:
            for char in line:
                if char == "#":
                    size += 1
        sizes[index] = size

result = 0
for region in regions:
    size, quantities = region.split(": ")
    width, length = [int(_) for _ in size.split("x")]
    quantities = [int(_) for _ in quantities.split()]

    region_size = width * length
    presents_size = 0
    max_size = 0
    for index in range(0, len(quantities)):
        presents_size += quantities[index] * sizes[index]
        max_size += 9 * quantities[index]

    if region_size >= max_size or region_size >= presents_size: # xd
        result += 1
    
print(result)
