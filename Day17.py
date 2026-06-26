#hashing
arr = [1, 2, 2, 3, 3, 3]
freq = {}

for i in arr:
    freq[i] = freq.get(i, 0) + 1

print(freq)

#set 
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)

#graph(bst)
from collections import deque

graph = {0: [1, 2], 1: [3], 2: [], 3: []}

q = deque([0])
visited = set()

while q:
    node = q.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        q.extend(graph[node])
