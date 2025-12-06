result = 0


def calculate(nums: list[str], op: str) -> int:
    expression = f"{nums[0]}"
    for num in nums[1:]:
        expression += op + num

    #print(expression)
    return eval(expression)


with open("input.txt", "r") as file:
    lines: list[str] = file.read().splitlines()

rows = len(lines)
cols = len(lines[0])

current_numbers: list[str] = []
current_operator = ""
for col in range(cols - 1, -1, -1):
    number = ""
    for row in range(0, rows - 1):
        number += lines[row][col]
    operator = lines[rows - 1][col]

    if number.strip() == "" and operator == " ":  # blank col
        if current_numbers:
            result += calculate(current_numbers, current_operator)
            current_numbers = []
    else:
        if number.strip():
            current_numbers.append(str(int(number.strip())))  # for leading zeros

        if operator in "+*":
            current_operator = operator

if current_numbers:
    result += calculate(current_numbers, current_operator)
print(result)
