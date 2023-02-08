import sys

input = sys.stdin.readline

r, c, w = map(int, input().split())

res = 0

d = [[1] * (i+1) for i in range(31)]
for i in range(2, 31):
  for j in range(1, i):
    d[i][j] = d[i - 1][j - 1] + d[i - 1][j]

for i in range(r - 1, r + w - 1):
  for j in range(c - 1, c + 1 + (i - r)):
    res += d[i][j]
    
print(res)
