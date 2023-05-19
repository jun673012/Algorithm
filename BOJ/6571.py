import sys

input = sys.stdin.readline

d = [1, 1]
for i in range(2, 1001):
  d.append(d[i-2] + d[i-1])

while True:
  a, b = map(int, input().split())
  if a == 0 and b == 0:
    break
  cnt = 0
  for i in range(1, 1001):
    if a <= d[i] and d[i] <= b:
      cnt += 1
  print(cnt)
