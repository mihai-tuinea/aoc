with open("input.txt", "r") as file:
    ranges: list[str] = (file.read()).split(",")

result = 0


def is_invalid(number: int) -> bool:
    s: str = str(number)
    n: int = len(s)
    mid: int = n // 2
    return n % 2 == 0 and s[:mid] == s[mid:]


def is_repeated_pattern(s: str) -> bool:
    n: int = len(s)
    for size in range(1, n // 2 + 1):
        if n % size == 0:
            substring: str = s[:size]
            if substring * (n // size) == s:
                return True
    return False


for segment in ranges:
    first, last = map(int, segment.split("-"))

    for i in range(first, last + 1):
        if is_repeated_pattern(str(i)):
            result += i

print(result)
