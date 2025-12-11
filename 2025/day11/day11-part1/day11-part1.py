connections: dict[str, list] = {}
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split()
        key = parts[0][:-1]

        connections[key] = []
        for val in parts[1:]:
            connections[key].append(val)


def dfs(current: str) -> int:
    if current == "out":
        return 1

    total = 0
    for val in connections.get(current, []):
        total += dfs(val)

    return total


print(dfs("you"))
