import sys

input = sys.stdin.readline

n = int(input())
l = [0]*10001
for _ in range(n):
  l[int(input())] += 1
for i in range(10001):
  if l[i] != 0:
    for _ in range(l[i]):
      print(i)
