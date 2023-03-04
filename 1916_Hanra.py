import heapq

# 이렇게 input을 받아들이는게 더 빠르다함.
import sys
input = sys.stdin.readline

# take the input

city = int(input())
bus = int(input())
maxCost = 100000000
graph = {i: [] for i in range(1, city+1)}
for _ in range(bus):
    start, dest, cost = map(int, input().split())
    graph[start].append((dest, cost))
s, g = map(int, input().split())

def minCostCal(s, graph):
    heap = [] # (total_cost, current_city)
    explore = [maxCost] * (city + 1)
    explore[s] = 0
    heapq.heappush(heap, (0, s))

    while heap:
        total, current = heapq.heappop(heap)
        if explore[current] < total:
            continue
        for (dest, cost) in graph[current]:
            totalCost = cost + total
            if explore[dest] > totalCost:
                explore[dest] = totalCost
                heapq.heappush(heap, (totalCost, dest))

    return explore[g]

result = minCostCal(s, graph)

print(result)