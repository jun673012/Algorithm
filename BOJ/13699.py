import sys

input = sys.stdin.readline
  
n = int(input())

d = [0] * 36
d[0] = 1
d[1] = 1
d[2] = 2

for i in range(3, n + 1):
  for j in range(i):
    d[i] += d[j] * d[i - j - 1]
print(d[n])
