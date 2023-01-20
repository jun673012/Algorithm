import sys

input = sys.stdin.readline

d = [0] * 1000001
d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 2
d[5] = 2

t = int(input())

for i in range(t):
  n = int(input())
  
  for i in range(5, n + 1):
      d[i] = d[i - 1] + d[i - 5]
  print(d[n])
  
