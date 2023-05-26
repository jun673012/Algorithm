import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))
up = max(t)
down = 1

while up >= down:
  s = (up+down) // 2
  tl = 0
  for i in t:
    if i > s:
      tl += i-s
  if tl >= m:
    down = s+1
  else:
    up = s-1
    
print(up)
