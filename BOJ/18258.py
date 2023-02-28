import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
  o = input().split()

  if o[0] == 'front':
    if not q:
      print(-1)
    else:
      print(q[0])
  elif o[0] == "back":
    if not q:
      print(-1)
    else:
      print(q[-1])
  elif o[0] == "empty":
    if not q:
      print(1)
    else:
      print(0)
  elif o[0] == "size":
    print(len(q))
  elif o[0] == "pop":
    if not q:
      print(-1)
    else:
      print(q.popleft())
  elif o[0] == 'push':
    q.append(o[1])
