import sys

input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))
r = [-1]*n
l = []

for i in range(n):
  while l and d[l[-1]] < d[i]:
    r[l.pop()] = d[i]
  l.append(i)
print(*r)
        
