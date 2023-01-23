import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 1000001
d[1] = 1
d[2] = 1

for i in range(3, abs(n) + 1):
  d[i] = (d[i - 1] + d[i - 2]) % 1000000000

if n < 0 and n % 2 == 0:
  print(-1)
elif n == 0:
  print(0)
else:
  print(1)
  
print(d[abs(n)])
