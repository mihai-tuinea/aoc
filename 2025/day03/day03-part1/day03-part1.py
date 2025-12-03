result: int = 0

with open("input.txt", "r") as file:
    for line in file:
        line: str = line.strip()

        highest: int = 11
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                current: int = int(line[i]) * 10 + int(line[j])
                if current > highest:
                    highest = current

        result += highest


print(result)
