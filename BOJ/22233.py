import sys

input = sys.stdin.readline

n, m = map(int, input().split())
blg = {}
for i in range(n):
  blg[input().rstrip()] = 1
cnt = len(blg)
for i in range(m):
  kw = input().rstrip().split(",")
  for i in kw:
    if i in blg.keys():
      if blg[i] == 1:
        blg[i] -= 1
        cnt -= 1
  print(cnt)
