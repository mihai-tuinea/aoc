with open("input.txt", "r") as file:
    ranges: list[str] = (file.read()).split(",")

result = 0


def is_invalid(number: int) -> bool:
    s: str = str(number)
    n: int = len(s)
    mid: int = n // 2
    return n % 2 == 0 and s[:mid] == s[mid:]


for segment in ranges:
    first, last = map(int, segment.split("-"))

    for i in range(first, last + 1):
        if is_invalid(i):
            result += i

print(result)
