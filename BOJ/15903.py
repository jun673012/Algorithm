import sys
from queue import PriorityQueue

input = sys.stdin.readline

que = PriorityQueue()

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
  que.put(i)
for _ in range(m):
  tmp = 0
  for _ in range(2):
    tmp += que.get()
  for _ in range(2):
    que.put(tmp)

res = 0
for i in range(n):
  res += que.get()
print(res)
