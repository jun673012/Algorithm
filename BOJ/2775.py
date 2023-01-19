import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    d = [i for i in range(1, n + 1)]
  
    for j in range(k):
        for k in range(1, n):
            d[k] += d[k - 1]
    print(d[-1])
