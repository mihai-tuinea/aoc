result = 0

with open("input.txt", "r") as file:
    content = []
    for line in file:
        line = line.strip()

        content.append(line.split())

numbers = content[:-1]
rows = len(numbers)
cols = len(numbers[0])
symbols = content[-1]

for i in range(0, len(symbols)):
    expression = f"{numbers[0][i]}"
    for row in range(1, rows):
        expression += symbols[i] + numbers[row][i]
    result += eval(expression)

print(result)
