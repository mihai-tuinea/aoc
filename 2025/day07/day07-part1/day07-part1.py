with open("input.txt", "r") as file:
    first_line = file.readline().strip()
    width = len(first_line)

    beams = set()  # indexes of active beams
    for i in range(len(first_line)):
        if first_line[i] == "S":
            beams.add(i)
            break

    result = 0

    for line in file:
        line = line.strip()

        for index in range(0, width):
            if line[index] == "^":
                if index in beams:
                    result += 1
                    beams.remove(index)
                if index > 0:
                    beams.add(index - 1)
                if index < width - 1:
                    beams.add(index + 1)

print(result)
