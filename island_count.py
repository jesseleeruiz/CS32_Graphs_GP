"""
Remember these steps to solve almost any graphs problem:
- Translate the problem into terminology you've learned this week
- Build your graph
- Traverse your graph


ISLANDS MATRIX CHALLENGE!
--------------------------
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:
islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]
island_counter(islands) # returns 4
traversal (define a function) => dft(row, col, matrix, visited) => returns visited
get neighbors (define function) => get_nieghbors(col, row, matrix) => check north south east and west for connections / x, y / col / row
each island is a vertex
each connection of north, south, east or west (edge)
"""

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def dft(row, column, matrix, visited):
    stack = Stack()

    stack.push((row, column))

    while stack.size() > 0:
        v = stack.pop()
        row = v[0]
        column = v[1]

        if not visited[row][column]:
            visited[row][column] = True
            for neighbor in get_neighbors(column, row, matrix):
                stack.push(neighbor)

    return visited

def get_neighbors(column, row, matrix):
    neighbors = []

    # Check North
    if row > 0 and matrix[row - 1][column] == 1:
        neighbors.append((row - 1, column))

    # Check South
    if row < len(matrix) - 1 and matrix[row + 1][column] == 1:
        neighbors.append((row - 1, column))

    # Check East
    if column < len(matrix[0]) - 1 and matrix[row][column + 1] == 1:
        neighbors.append((row, column + 1))

    # Check West
    if column > 0 and matrix[row][column - 1] == 1:
        neighbors.append((row, column - 1))

    return neighbors

def island_counter(matrix):
    # Create a visited matrix and counter
    visited = []
    counter_of_islands = 0

    # Adding a bunch of falses to the visited to show none of them are visited.
    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0])) 

    # Walk through each of the cells in the matrix and see if it has been visited
    for column in range(len(matrix[0])):
        for row in range(len(matrix)):

            # If not visited
            if not visited[row][column]:

                # Keep going until you reach a 1
                if matrix[row][column] == 1:

                    # Then do a DFT and mark each as visited
                    visited = dft(row, column, matrix, visited)

                    # Increment counter by 1
                    counter_of_islands += 1

                else:
                    visited[row][column] = True

    return counter_of_islands


if __name__ == "__main__":
    islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

    print(island_counter(islands))  # 4

    islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

    print(island_counter(islands))  # 13

