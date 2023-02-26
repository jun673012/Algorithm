import sys

input = sys.stdin.readline

n = int(input())
x = [0] * n

for i in range(n):
  x[i] = list(map(int ,input().split()))
x.sort()

for i in range(n):
  print(x[i][0], x[i][1])
