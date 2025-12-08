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
        if not line:
            continue
        x, y, z = line.split(",")
        boxes.append(Box(int(x), int(y), int(z)))

connections: list[tuple] = []  # (index_1, index_2, distance)
num_boxes = len(boxes)

for i in range(num_boxes):
    for j in range(i + 1, num_boxes):
        distance = boxes[i].distance_to(boxes[j])
        connections.append((i, j, distance))

G = nx.Graph()
G.add_nodes_from(range(num_boxes))
G.add_weighted_edges_from(connections)

mst_edges = list(nx.minimum_spanning_edges(G, algorithm="kruskal", data=False))
last_i, last_j = mst_edges[-1]

result = boxes[last_i].x * boxes[last_j].x
print(result)
