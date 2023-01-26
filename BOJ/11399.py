import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
res = 0
p.sort()

for i in range(n):
  for j in range(i + 1):
    res += p[j]
    
print(res)
