import sys

input = sys.stdin.readline



n = int(input())
cn = list(map(int, input().split()))
m = int(input())
sc = list(map(int, input().split()))

res = {}

for i in cn:
  if i in res:
    res[i] += 1
  else:
    res[i] =1

for i in sc:
  if i in res:
    print(res[i], end=" ")
  else:
    print(0, end=" ")
