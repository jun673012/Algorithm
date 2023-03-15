import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
  
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny <0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    return cnt
  
n = int(input())

graph = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      cnt.append(bfs(i, j))
    
cnt.sort()

print(len(cnt))
print(*cnt, sep='\n')
