import logging
from os import path
from typing import List
from pprint import pprint
import sys

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

file = "day12/input.txt"
nodes = {}

sys.setrecursionlimit(1500)

def is_small_cave(node: str) -> bool:
    return node == node.lower()

def find_path(current_node: str, nodes: dict, path: List[str], paths: List[List[str]] ) -> List[str]:
    path.append(current_node)
    log.debug(f"current_node: {current_node}")
    log.debug(f"path: {path}")
    for node in nodes[current_node]:
        if node == "start":
            continue
        if node == "end":
            path.append(node)
            paths.append(path)
            continue
        if not is_small_cave(node):
            new_path = path.copy()
            find_path(node, nodes, new_path, paths)
            continue
        if is_small_cave(node) and node not in path:
            new_path = path.copy()
            find_path(node, nodes, new_path, paths)
            continue


    

with open(file) as f:
    for line in f:
        x, y = line.strip().split('-')
        if x not in nodes:
            nodes[x] = []
        if y not in nodes:
            nodes[y] = []
        nodes[x].append(y)
        nodes[y].append(x)

pprint(nodes)
paths = []
path = []
find_path("start", nodes, path, paths)
pprint([",".join(path) for path in paths])
print(len(paths))