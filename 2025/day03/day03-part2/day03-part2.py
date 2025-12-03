from collections import deque

result: int = 0


def highest(line: str, k: int = 12):
    to_delete: int = len(line) - k
    result_digits: deque = deque()

    for digit in line:
        while len(result_digits) > 0 and result_digits[-1] < digit and to_delete > 0:
            result_digits.pop()
            to_delete -= 1
        result_digits.append(digit)

    while to_delete > 0:
        result_digits.pop()
        to_delete -= 1

    return int("".join(result_digits))


with open("input.txt", "r") as file:
    for line in file:
        line: str = line.strip()

        result += highest(line, 12)


print(result)
