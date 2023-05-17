import sys
import heapq

input = sys.stdin.readline

n = int(input())
c = []
res = 0

for i in range(n):
  c.append(int(input()))
  
heapq.heapify(c)

while len(c) > 1:
  t = heapq.heappop(c) + heapq.heappop(c)
  res += t
  heapq.heappush(c, t)
  
print(res)
