count = 0
ranges = []

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

ranges = sorted(ranges)
current_l, current_h = ranges[0]
for next_l, next_h in ranges[1:]:
    if current_h + 1 >= next_l:  # +1 in case of consecutive nums
        current_h = max(current_h, next_h)
    else:
        count += current_h - current_l + 1
        current_l, current_h = next_l, next_h

count += current_h - current_l + 1

print(count)
