import sys

input = sys.stdin.readline

n, ns, p = map(int, input().split())
if n == 0:
  print(1)
else:
  rnk = list(map(int, input().split()))
  if n == p and rnk[-1] >= ns:
    print(-1)
  else:
    res = n+1
    for i in range(n):
      if rnk[i] <= ns:
        res = i+1
        break
    print(res)
