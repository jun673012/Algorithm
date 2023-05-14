import sys

input = sys.stdin.readline

def dfs(x, y):
    if graph[x][y] == '-':
      graph[x][y] = 1
      for dy in [-1, 1]:
        Y = y + dy
        if (Y > 0 and Y < m) and graph[x][Y] == '-':
          dfs(x, Y)
          
    if graph[x][y] == '|':
      graph[x][y] = 1
      for dx in [-1, 1]:
        X = x + dx
        if (X > 0 and X < n) and graph[X][y] == '|':
          dfs(X, y)

n, m = map(int, input().split())
cnt = 0
graph = []
for _ in range(n):
  graph.append(list(input()))
  
for i in range(n):
  for j in range(m):
    if graph[i][j] == '-' or graph[i][j] == '|':
      dfs(i,j)
      cnt += 1

print(cnt)
