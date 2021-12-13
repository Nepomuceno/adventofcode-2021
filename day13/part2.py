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

def num_of_times_in_path(node: str, paths: List[str]) -> int:
    return paths.count(node)

def find_path(current_node: str, nodes: dict, path: List[str], paths: List[List[str]], allowed_multiple: str ) -> List[str]:
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
            find_path(node, nodes, new_path, paths, allowed_multiple)
            continue
        if node == allowed_multiple and num_of_times_in_path(node, path) < 2:
            new_path = path.copy()
            find_path(node, nodes, new_path, paths, allowed_multiple)
            continue
        if is_small_cave(node) and node not in path:
            new_path = path.copy()
            find_path(node, nodes, new_path, paths, allowed_multiple)
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

global_paths = []
pprint(nodes)
small_caves = [node for node in nodes if is_small_cave(node) and node != "start" and node != "end"] 
for node in small_caves:
    paths = []
    path = []
    find_path("start", nodes, path, paths, node)
    global_paths = global_paths +  paths
global_paths = dict.fromkeys([",".join(path) for path in global_paths])
pprint(global_paths)
print(len(global_paths))