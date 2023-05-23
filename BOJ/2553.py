import sys
from math import factorial

input = sys.stdin.readline

n = int(input())

a = str(factorial(n))
for i in a[::-1]:
  if i == '0':
    continue
  else:
    print(i)
    break
