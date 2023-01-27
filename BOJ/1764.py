import sys

input = sys.stdin.readline

n, m = map(int, input().split())
d = set()
b = set()

for _ in range(n):
  d.add(input())
for _ in range(m):
  b.add(input())

res = sorted(list(d & b))

print(len(res))
print(*res, sep='')
