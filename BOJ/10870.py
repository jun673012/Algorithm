import sys

input = sys.stdin.readline

n = int(input())

def f(n):
  if n <= 1:
    return n
  return f(n-1) + f(n-2)

print(f(n))
