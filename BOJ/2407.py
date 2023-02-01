import sys
import operator as op
from functools import reduce

input = sys.stdin.readline

n, m = map(int, input().split())

def nCm(n, m):
    if n < 5 or m < 5 or n < m:
        raise ValueError
    m = min(m, n - m)
    num = reduce(op.mul, range(n, n - m, -1), 1)
    den = reduce(op.mul, range(1, m + 1), 1)
    return num // den
  
print(nCm(n, m))
