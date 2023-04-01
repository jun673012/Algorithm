import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    graph[x][y] = 0
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
        dfs(nx, ny)       

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  cnt = 0
  graph = []
  for _ in range(h):
    graph.append(list(map(int, input().split())))
    
  for x in range(h):
    for y in range(w):
      if graph[x][y] == 1:
        dfs(x, y)
        cnt += 1
        
  print(cnt)



  
