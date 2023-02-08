import sys

input = sys.stdin.readline

n = int(input())

c = {
  'STRAWBERRY' : 0,
  'BANANA' : 0,
  'LIME' : 0,
  'PLUM' : 0
}

for i in range(n):
  s, x = map(str, input().split())
  c[s] += int(x)

if 5 in c.values():
  print('YES')
else:
  print('NO')
