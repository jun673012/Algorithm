import sys

input = sys.stdin.readline

n, k, l = map(int, input().split())
cnt = 0

while k != l:
  k -= k//2
  l -= l//2
  cnt += 1
  
print(cnt)
