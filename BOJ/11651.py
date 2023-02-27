import sys

input = sys.stdin.readline

n = int(input())
x = []

for i in range(n):
  x.append(list(map(int ,input().split())))
  
x.sort(key=lambda x: (x[1], x[0]))

for i in x:
  print(i[0], i[1])
  
