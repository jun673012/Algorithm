import sys
from collections import deque

input = sys.stdin.readline
          
def bfs(a):
    queue = deque([a])
    visited[a] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
                s[i] = s[v]+1

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
s = [0] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
bfs(a)
print(s[b] if s[b] > 0 else -1)
