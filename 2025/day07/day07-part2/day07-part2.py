with open("input.txt", "r") as file:
    first_line = file.readline().strip()
    width = len(first_line)

    beams: dict = {}  # index: count
    for i in range(0, len(first_line)):
        if first_line[i] == "S":
            beams[i] = 1
            break

    for line in file:
        line = line.strip()
        next_beams: dict = {}

        for index in range(0, width):
            count = beams.get(index, 0)

            if line[index] == "^":
                if index > 0:
                    next_beams[index - 1] = next_beams.get(index - 1, 0) + count
                if index < width - 1:
                    next_beams[index + 1] = next_beams.get(index + 1, 0) + count
            else:
                next_beams[index] = next_beams.get(index, 0) + count

        beams = next_beams

result = 0
# beams that made it to last line
for index, count in beams.items():
    result += count

print(result)
