import sys

input = sys.stdin.readline

n = int(input())
r = list(map(int, input().split()))
f = list(map(int, input().split()))

cnt = 0
a = f[0]

for i in range(n - 1):
  if f[i] < a:
    a = f[i]
  cnt += a * r[i]
    
print(cnt)
