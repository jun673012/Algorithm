import sys

input = sys.stdin.readline

n = list(map(int, input().split()))

for i in range(0, len(n) - 1):
  for j in range(0, len(n) - 1):
    if n[j] > n[j + 1]:
      n[j], n[j + 1] = n[j + 1], n[j]
      print(*n)
