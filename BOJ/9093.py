import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  a = list(input().split())
  for i in a:
    print(i[::-1], end=" ")
  print()
