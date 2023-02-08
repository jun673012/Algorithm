import sys

input = sys.stdin.readline

d = [1] * 1000001
d[1] = 1
d[2] = 2

t = int(input())

for i in range(3, 1000001):
  d[i] = (d[i - 1]+ d[i - 2] + d[i - 3]) % 1000000009  
  
for i in range(t):
  n = int(input())
  print(d[n] % 1000000009)
