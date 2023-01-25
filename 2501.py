import sys

input = sys.stdin.readline

n, k = map(int, input().split())
res = []

for i in range(1, n + 1):
  if n % i == 0:
    res.append(i)
    
if len(res) < k:
  print(0)
else:
  print(res[k -1 ])
