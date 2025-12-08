import math
import networkx as nx


class Box:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other: "Box") -> float:
        dist_x = (other.x - self.x) ** 2
        dist_y = (other.y - self.y) ** 2
        dist_z = (other.z - self.z) ** 2
        return math.sqrt(dist_x + dist_y + dist_z)


boxes: list[Box] = []
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        x, y, z = line.split(",")
        boxes.append(Box(int(x), int(y), int(z)))

connections: list[tuple] = []  # (index_1, index_2, distance)
num_boxes = len(boxes)

for i in range(num_boxes):
    for j in range(i + 1, num_boxes):
        distance = boxes[i].distance_to(boxes[j])
        connections.append((i, j, distance))

connections.sort(key=lambda x: x[2])
# LIMIT = 10
LIMIT = 1000
closest_connections = connections[:LIMIT]

G = nx.Graph()
G.add_nodes_from(range(num_boxes))
edges = [(i, j) for i, j, _ in closest_connections]
G.add_edges_from(edges)

circuits: list[set] = list(nx.connected_components(G))
sizes = [len(c) for c in circuits]
sizes.sort(reverse=True)

result = sizes[0] * sizes[1] * sizes[2]
print(result)
