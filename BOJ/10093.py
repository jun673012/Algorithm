import sys
input = sys.stdin.readline

a, b = map(int, input().split())

c = max(a, b)
d = min(a, b)
e = c - d - 1

if e + 1 < 1:
  e = 0
print(e)
  
for i in range(d + 1, c):
  print(i, end=' ')
