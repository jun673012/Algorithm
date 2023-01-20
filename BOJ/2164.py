import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque([i + 1 for i in range(n)])

while(len(q) > 1):
  q.popleft()
  tmp = q.popleft()
  q.append(tmp)
  
print(q[0])
