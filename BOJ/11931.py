import sys

input = sys.stdin.readline

n = int(input())
d = []

for _ in range(n):
    d.append(int(input()))
  
d.sort(reverse=True)

for i in d:
  print(i)
