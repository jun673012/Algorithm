import sys

input = sys.stdin.readline

t = int(input())

d = [1] * 70
d[2] = 2
d[3] = 4

for i in range(t):
  n = int(input())
  
  for i in range(4, n + 1):
    d[i] = d[i - 1] + d[i - 2] + d[i - 3] + d[i - 4]
  print(d[n])
