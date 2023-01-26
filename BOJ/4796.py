import sys

input = sys.stdin.readline

i = 0

while True:
  vc = 0
  L, P, V = map(int, input().split())
  if L == P == V == 0:
    break

  vc += (V // P) * L + min(V % P, L)
  i += 1
  
  print('Case %d: %d' %(i, vc))
