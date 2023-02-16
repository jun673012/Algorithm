import sys

input = sys.stdin.readline

a, b = map(int, input().split())

c = []
res = 0

for i in range(1, b + 1):
  for _ in range(i):
    c.append(i)

for i in range(a - 1, b):
  res += c[i]

print(res)
