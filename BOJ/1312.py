import sys

input = sys.stdin.readline

a, b, n = map(int, input().split())

for _ in range(n):
  a = (a % b) * 10
  res = a // b
print(res)
