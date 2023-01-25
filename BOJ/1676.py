import sys
import math

input = sys.stdin.readline

n = int(input())

cnt = 0
n = math.factorial(n)

for i in range(len(str(n))):
  if n % 10 == 0:
    n = n // 10
    cnt += 1
  else:
    break
    
print(cnt)
