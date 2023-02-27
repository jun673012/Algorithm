import sys

input = sys.stdin.readline

n = int(input())
x = []

for i in range(n):
  x.append(list(map(str ,input().split())))
  
x.sort(key=lambda x: int(x[0]))

for i in x:
  print(i[0], i[1])
