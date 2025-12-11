from functools import cache

connections: dict[str, list] = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split()
        key = parts[0][:-1]

        connections[key] = []
        for val in parts[1:]:
            connections[key].append(val)


@cache  # memoization so it doesnt finish executing in 5 billion hours
def dfs(current: str, found_dac: bool, found_fft: bool) -> int:
    if current == "out":
        if found_dac and found_fft:
            return 1
        return 0

    total = 0
    for val in connections.get(current, []):
        total += dfs(val, found_dac or val == "dac", found_fft or val == "fft")

    return total


print(dfs("svr", False, False))
