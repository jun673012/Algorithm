import sys

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
cnt = 1
for i in range(n-1):
  if h[i] > h[i+1]:
    continue
  cnt += 1
print(cnt)
