import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pw = {}

for _ in range(n):
  key, val = map(str, input().split())
  pw[key] = val
for _ in range(m):
  sa = str(input().rstrip())
  print(pw[sa])
