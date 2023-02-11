import sys

input = sys.stdin.readline

n = int(input())

_len = len(str(n))
res = 0

for i in range(_len - 1):
  res += 9 * 10 ** i * (i + 1)

print(res + (n - 10 ** (_len - 1) + 1) * _len)
