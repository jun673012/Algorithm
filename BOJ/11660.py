import sys

input = sys.stdin.readline

n, m = map(int,input().split())
d = [list(map(int, input().split())) for _ in range(n)]

a = [[0] * (n+1) for i in range(n+1)]

for i in range(1, n+1):
  for j in range(1, n+1):
    a[i][j] = a[i][j-1] + a[i-1][j] + d[i-1][j-1] - a[i-1][j-1]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(a[x2][y2] - a[x1-1][y2] - a[x2][y1-1] + a[x1-1][y1-1])
