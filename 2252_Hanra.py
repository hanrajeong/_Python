number, compare = map(int, input().split())
graph = {i : [] for i in range(number+1)}
degree = [0] * (number + 1)

for _ in range(compare):
    s, e = map(int, input().split())
    graph[s].append(e)
    degree[e] += 1
stack = []
result = []
for i in range(1, number+1):
    if degree[i] == 0:
        stack.append(i)
while stack:
    current = stack.pop()
    result.append(current)
    for adjNode in graph[current]:
        degree[adjNode] -= 1
        if degree[adjNode] == 0:
            stack.append(adjNode)

print(" ".join(str(r) for r in result))