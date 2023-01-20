import sys

input = sys.stdin.readline

d = [1] * 46

def fibo(x):
    for i in range(2, n+1):
        d[i] = d[i-1] + d[i-2]
    return d[x]

t = int(input())

for i in range(t):
  n = int(input())
  print(fibo(n))
