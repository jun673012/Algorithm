import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
d = deque()
for i in range(n):
  a = list(input().split())
  if a[0] == "push_front":
    d.appendleft(a[1])
  elif a[0] == "push_back":
    d.append(a[1])
  elif a[0] == "pop_front":
    if len(d) == 0:
      print(-1)
    else:
      print(d.popleft())
  elif a[0] == "pop_back":
    if len(d) == 0:
      print(-1)
    else:
      print(d.pop())
  elif a[0] == "size":
    print(len(d))
  elif a[0] == "empty":
    print(1 if len(d) == 0 else 0)
  elif a[0] == "front":
    if len(d) == 0:
      print(-1)
    else:
      print(d[0])
  else:
    if len(d) == 0:
      print(-1)
    else:
      print(d[-1])
