import sys

input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
m = int(input())

s, e = 0, max(b)

while s <= e:
  mid = (s+e) // 2
  t = 0
  for i in b:
    t += min(mid, i)
  if t <= m:
    s = mid+1
  else:
    e = mid-1
print(e)
