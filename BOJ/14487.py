import sys

input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))

sum = 0

for i in v:
  sum += i

print(sum - max(v))
