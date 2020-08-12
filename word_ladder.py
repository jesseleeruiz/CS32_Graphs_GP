from queue import Queue

f = open('words.txt')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get Neighbors
def get_neighbors(word):
    neighbors = []

    # Turn our word into a letters list
    string_word = list(word)

    # For each of the letters; Iterate
    for index in range(len(string_word)):

        # Swap this letter with each letter in alphabet
        for letter in letters:
            temp_word = list(string_word)
            temp_word[index] = letter
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors

# BFS with path
def find_ladders(begin_word, end_word):
    queue = Queue()
    visited = set()
    queue.enqueue([begin_word])

    while queue.size() > 0:
        path = queue.dequeue()
        vertex = path[-1]

        if vertex not in visited:
            visited.add(vertex)
            if vertex == end_word:
                return path

            for neighbor in get_neighbors(vertex):
                path_copy = list(path)
                path_copy.append(neighbor)
                queue.enqueue(path_copy)
