import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
d = deque(enumerate(map(int, input().split())))
l = []

while d:
  a, b = d.popleft()
  l.append(a+1)
  if b > 0:
    d.rotate(-(b-1))
  else:
    d.rotate(-b)
print(*l)
