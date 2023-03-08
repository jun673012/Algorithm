import sys
from collections import deque

input = sys.stdin.readline

def dfs(s):
    visited[s] = True
    print(s, end=" ")

    for i in graph[s]:
        if not visited[i]:
            dfs(i)
          
def bfs(s):
    queue = deque([s])
    visited[s] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
  
visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)
