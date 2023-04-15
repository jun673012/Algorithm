import sys

input = sys.stdin.readline

n = int(input())
c = []
res = 0
for _ in range(n):
  c.append(int(input()))
c.sort(reverse=True)

for i in range(n):
  if (i+1) % 3 == 0:
    continue
  res += c[i]

print(res)
