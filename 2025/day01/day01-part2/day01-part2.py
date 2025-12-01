current: int = 50
count: int = 0

with open("input.txt", "r") as file:
    for line in file:
        line: str = line.strip()

        direction: str = line[0]
        distance: int = int(line[1:])

        for _ in range(distance):
            if direction == "R":
                current = (current + 1) % 100
            elif direction == "L":
                current = (current - 1) % 100

            if current == 0:
                count += 1

print(count)
