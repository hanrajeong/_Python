import sys
input = sys.stdin.readline
import heapq

V, E = map(int, input().split())
# graph = {i : [] for i in range(1, V+1)}
heap = []
for _ in range(E):
    A, B, C = map(int, input().split())
    # graph[A].append((B, C))
    # graph[B].append((A, C))
    heapq.heappush(heap, (C, A, B))

result = 0
parent = [i for i in range(V+1)]

def find_parent(parent, current):
    if parent[current] != current:
        parent[current] = find_parent(parent, parent[current])
    return parent[current]

def update_parent(parent, first, second):
    firstParent = find_parent(parent, first)
    secondParent = find_parent(parent, second)
    if firstParent < secondParent:
        parent[secondParent] = firstParent
    else:
        parent[firstParent] = secondParent

while heap:
    cost, first, second = heapq.heappop(heap)
    # if they have the same parent -> meaning they form the cycle
    if find_parent(parent, first) == find_parent(parent, second):
        continue
    # if not, add the edge and update the parent
    else:
        update_parent(parent, first, second)
        result += cost

print(result)