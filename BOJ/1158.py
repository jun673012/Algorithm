import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
y = deque()

for i in range(1, n + 1):
  y.append(i)

while y:
  for _ in range(k - 1):
    y.append(y.popleft())
  arr.append(y.popleft())
  
print(str(arr).replace('[', '<').replace(']', '>'))
