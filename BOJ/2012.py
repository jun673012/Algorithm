import sys

input = sys.stdin.readline

n = int(input())
s = 0
r = []
for _ in range(1, n+1):
  r.append(int(input()))
r.sort()

for i in range(1, n+1):
  s += abs(i-r[i-1])
print(s)
