n = int(input())
t = int(input())

graph = [[] for _ in range(n + 1)]

visited = [False] * len(graph)

for i in range(t):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(sum(visited)-1)
