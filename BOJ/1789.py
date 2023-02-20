import sys

input = sys.stdin.readline

s = int(input())
n = 0
b = 0

while True:
  b += 1
  n += b
  if n > s:
    break

print(b - 1)
  
