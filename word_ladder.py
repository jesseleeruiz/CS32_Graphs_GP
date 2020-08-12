from queue import Queue

<<<<<<< HEAD
f = open('words.txt')
words = f.read().split("\n")
f.close()

=======

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()


>>>>>>> 8929add019cea0adee0aedf26f1a100e6ccacd44
word_set = set()
for word in words:
    word_set.add(word.lower())

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

<<<<<<< HEAD
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
=======
# get neighbors
def get_neighbors(word):
    neighbors = []
    # turn our word in to a letters list
    letters_list = list(word)

    # for each letters
    for i in range(len(letters_list)): # O(n)
        # swap each letter
        for letter in letters: # O(1)
            temp_word = list(letters_list)
            temp_word[i] = letter
>>>>>>> 8929add019cea0adee0aedf26f1a100e6ccacd44
            w = "".join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors

<<<<<<< HEAD
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
=======
# BFS with path (Search)
def find_ladders(begin_word, end_word):
    q = Queue()
    visited = set()
    # begin_word = begin_word.lower()
    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)
            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

print(find_ladders("sAil", "boat"))  # ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
print(find_ladders("hit", "cog"))  # ['hit', 'hot', 'cot', 'cog']
print(find_ladders("hungry", "happy"))  # None
print(find_ladders("abel", "ewes")) # ['abel', 'axel', 'axes', 'exes', 'ewes']
>>>>>>> 8929add019cea0adee0aedf26f1a100e6ccacd44
