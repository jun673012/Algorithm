import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 3

for i in range(3, 1001):
  d[i] = (d[i - 1] + d[i - 2] + d[i - 2]) % 10007
  
print(d[n])
