import sys

input = sys.stdin.readline

n, l = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
for i in range(n):
  if l >= h[i]:
    l += 1
  else:
    break

print(l)
