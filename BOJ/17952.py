import sys

input = sys.stdin.readline

n = int(input())
res = 0
s = []

for _ in range(n):
  s.append(list(map(int, input().split())))
  if s[-1][0] == 0:
    s.pop()
  if s:
    s[-1][2] -= 1
    if s[-1][2] == 0:
      res += s[-1][1]
      s.pop()
      
print(res)
