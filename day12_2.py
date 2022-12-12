from sys import argv
from sys import maxsize
import numpy as np
from day12_class import Graph
script, input = argv

raw_data = open(input).read()
data = raw_data.split('\n')
height_map = np.zeros((len(data), len(data[0])))

low_points = []
for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        height = (-ord(data[i][j])) + 122
        if height == 39:
            start_coords = i, j
            height = 25
        elif height == 53:
            end_coords = i, j
            height = 0
        height_map[i][j] = height
        if height_map[(i,j)] == 25:
            low_points.append((i,j))

# Create graph
nodes = {}
for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        nodes[(i,j)] = Graph((i,j))
        adjacent = [(i-1, j), (i+1, j),(i, j-1),(i, j+1)]
        for k in range(0, len(adjacent)):
            if -1 < adjacent[k][0] < len(data) and -1 < adjacent[k][1] < len(data[0]):
                value = height_map[adjacent[k]]
                if value - height_map[i, j] <= 1:
                    nodes[(i,j)].add_neighbour((adjacent[k]))

all_pos = []
for key in nodes:
    all_pos.append(key)

# Dijkstra
unvisited_nodes = list(all_pos)
shortest_path = {}
previous_nodes = {}
for node in unvisited_nodes:
    shortest_path[node] = 100000000
shortest_path[end_coords] = 0

while unvisited_nodes:
    current_min_node = None
    for node in unvisited_nodes:
        if current_min_node == None:
            current_min_node = node
        elif shortest_path[node] < shortest_path[current_min_node]:
            current_min_node = node
    neighbours = nodes[current_min_node].get_neighbours()
    for neighbour in neighbours:
        tentative_value = shortest_path[current_min_node] + 1
        if tentative_value < shortest_path[neighbour]:
            shortest_path[neighbour] = tentative_value
            previous_nodes[neighbour] = current_min_node
    unvisited_nodes.remove(current_min_node)

shortest_shortest_path = 1000000
for point in low_points:
    if shortest_path[point] < shortest_shortest_path:
        shortest_shortest_path = shortest_path[point]
print(shortest_shortest_path)