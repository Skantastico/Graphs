# import Queue from util in graphs

import sys
sys.path.append("projects/graph")
from util import Queue


def get_ancestor(ancestors, child):
    heirs = []
    for heir in ancestors:
        if heir[1] == child:
            heirs.append(heir[0])
    return heirs


def earliest_ancestor(ancestors, starting_node):
    # starting conditions
    q = Queue()
    q.enqueue([starting_node])
    visited = set()
    path_len = 1
    oldest_parent = -1

    # while loop to search
    while q.size() > 0:
        path = q.dequeue()
        current_node = path[-1]

        if current_node not in visited:
            visited.add(current_node)

        if len(path) >= path_len and current_node < oldest_parent or \
        len(path) > path_len:
            path_len = len(path)
            oldest_parent = current_node

        for parent in get_ancestor(ancestors, current_node):
            path_copy = list(path)
            path_copy.append(parent)
            q.enqueue(path_copy)

    return oldest_parent
