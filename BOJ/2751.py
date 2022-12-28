import sys

input = sys.stdin.readline

n = int(input())

a = [0 for _ in range(n)]

for i in range(n):
  a[i] = int(input())
  
a.sort()

for i in range(n):
  print(a[i])
