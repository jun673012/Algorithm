import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  que = deque(list(map(int, input().split())))
  cnt = 0
  while que:
    mq = max(que)
    p = que.popleft()
    m -= 1
    if mq == p:
      cnt += 1
      if m < 0:
        print(cnt)
        break
    else:
      que.append(p)
      if m < 0:
        m = len(que) - 1 
