import sys

input = sys.stdin.readline

u = list(map(int, input().split()))
s = list(map(int, input().split()))

us = 0
ss = 0

for i in range(9):
  us += u[i]

  if us > ss:
    print('Yes')
    break
  elif i == 8 and us <= ss:
    print('No')
  ss += s[i]
