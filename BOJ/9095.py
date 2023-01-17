import sys

input = sys.stdin.readline

d = [0] * 1001
d[1] = 1
d[2] = 2
d[3] = 4

t = int(input())
for i in range(t):
  n = int(input())
  
  for i in range(4, 1001):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3]
  print(d[n])
