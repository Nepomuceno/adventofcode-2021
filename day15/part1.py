import logging
from typing import List, Tuple

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

file = "day15/input.txt"

with open(file) as f:
    lines = [line.strip() for line in f.readlines()]
    matrix = []
    for line in lines:
        matrix.append(list(line))
    graph = Graph()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            key = f"{i},{j}"
            if i > 0:
                graph.add_edge(key, f"{i-1},{j}", int(matrix[i-1][j]))
            if j > 0:
                graph.add_edge(key, f"{i},{j-1}", int(matrix[i][j-1]))
            if i < len(matrix) - 1:
                graph.add_edge(key, f"{i+1},{j}", int(matrix[i+1][j]))
            if j < len(matrix[i]) - 1:
                graph.add_edge(key, f"{i},{j+1}", int(matrix[i][j+1]))

path = dijsktra(graph, "0,0", f"{len(matrix)-1},{len(matrix[0])-1}")
print(path)
# sum of weights of the path
print(sum([graph.weights[(path[i], path[i+1])] for i in range(len(path) - 1)]))
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if f"{i},{j}" in path:
            print("X", end="")
        else:
            print(matrix[i][j], end="")
    print()
