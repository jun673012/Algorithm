import sys

input = sys.stdin.readline

n = int(input())

a = [i + 1 for i in range(n)]
b = []

while len(a) != 1:
  b.append(a.pop(0))
  a.append(a.pop(0))
  
print(*b + a, end=' ')
