import sys

input = sys.stdin.readline

n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))
l.sort()
print(*l, sep="\n")
