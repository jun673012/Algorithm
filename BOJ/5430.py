import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
lst = []
for _ in range(t):
  a = input().rstrip()
  n = int(input())
  que = deque(input().rstrip()[1:-1].split(","))
  c = 0
  
  if n == 0:
    que = []
  for i in a:
    if i == "R":
      c += 1
    elif i == "D":
      if len(que) == 0:
        c = 1
        print("error")
        break
      else:
        if c%2 == 1:
          que.pop()
        else:
          que.popleft()        
  else:
    if c%2 == 1:
      que.reverse()
    print("[" + ",".join(que) + "]")
