import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pkk = {}
pkv = {}

for i in range(n):
  key = input().rstrip()
  pkv[i + 1] = key
  pkk[key] = i + 1
  
for _ in range(m):
  s = input().rstrip()
  if s.isdigit():  
    print(pkv[int(s)])
  else:
    print(pkk[s])
