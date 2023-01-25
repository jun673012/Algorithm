import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = []
res = 0

for _ in range(n):
  a.append(int(input()))

for i in reversed(range(n)):
  res += k // a[i]
  k %= a[i]
  
print(res)
