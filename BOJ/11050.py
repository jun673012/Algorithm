import sys

input = sys.stdin.readline

n, k = map(int, input().split())

d = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    d[i][0] = 1
for i in range(k + 1):
    d[i][i] = 1
for i in range(1, n + 1):
    for j in range(1, k + 1):
        d[i][j] = d[i - 1][j] + d[i - 1][j - 1]
      
print(d[n][k])
