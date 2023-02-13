import sys

input = sys.stdin.readline

n = int(input())

res = 0
i = 1

while n >= 0:
  n -= i
  if i % 2 == 1:
    if n < 0:
      res = 0 - n
  i += 1
  
print(res)
