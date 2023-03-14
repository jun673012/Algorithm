import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n, m = map(int, input().split())
graph = [[] * i for i in range(n+1)]
visited = [False] * (len(graph)+1)
cnt = 0

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for i in range(1, n+1):
  if not visited[i]:
    if not graph[i]:
      cnt += 1
      visited[i] = True
    else:
      bfs(i)
      cnt += 1
  
print(cnt)
