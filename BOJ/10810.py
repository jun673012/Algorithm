import sys

input = sys.stdin.readline

n, m = map(int, input().split())
b = [0] * n
for _ in range(m):
  i, j, k = map(int, input().split())
  for a in range(i-1, j):
    b[a] = k
print(*b)
