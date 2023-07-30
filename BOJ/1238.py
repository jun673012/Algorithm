import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(s):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_idx, node_cost in graph[now]:
            cst = dist + node_cost

            if distance[node_idx] > cst:
                distance[node_idx] = cst
                heapq.heappush(q, (cst, node_idx))

    return distance


result = 0
for i in range(1, v + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)
