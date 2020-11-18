'''
Write a function that takes a 2D binary array and returns the number
of 1 islands.  An island consists of 1s that are connected to the
north, south, east, or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4

# UPER
## 1. Describe the problem in graphs terminology
##--What are our nodes?
##--What are our edges? When are nodes connected?
###--Each (x, y) in the array
####--If its a 1? or we only operate on the 1s

## What are our edges? When are nodes connected?
### A: They are connected when a direct neighbor is a 1

## Island in graph terms?
### Connected Component

## 2. Build your own graph or write getNeighbors

## 3. Choose your fighter(s)

##How to count the number of connected components?
## Get to each island, traverse teh component, then continue from where you were
##---Keep track of which nodes have already been traversed.

### Go through the array node by node, then check north, east, south, west
'''

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def getNeighbors(row, col, matrix):

    neighbors = []

    if col >= 1:
        west_neighbor = matrix[row][col - 1]
        if west_neighbor == 1:
            neighbors.append((row, col -1))

    if col <= len(matrix) - 2:
        east_neighbor = matrix[row][col + 1]
        if east_neighbor == 1:
            neighbors.append((row, col +1 ))

    if row <= len(matrix) - 2:
        south_neighbor = matrix[row + 1][col]
        if south_neighbor == 1:
            neighbors.append((row + 1, col))

    if row >= 1:
        north_neighbor = matrix[row - 1][col]
        if north_neighbor == 1:
            neighbors.append((row -1, col))

    return neighbors


def dft_recursive(row, col, visited, matrix):
    if (row, col) not in visited:
        visited.add((row, col))

        neighbors = getNeighbors(row, col, matrix)

        for neighbor in neighbors:
            dft_recursive(neighbor[0], neighbor[1], visited, matrix)

def count_islands(matrix):
    visited = set()
    connected_components = 0

    # iterate over matrix
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            node = matrix[row][col]

    # if 0 continue,
            if node == 0:
                continue
    # if 1: hold place, traverse and add to each visited, then go back
            elif node == 1:
                if (row, col) not in visited:
                    connected_components += 1
                    dft_recursive(row, col, visited, matrix)

    return connected_components


print(count_islands(islands)) # should return 4
