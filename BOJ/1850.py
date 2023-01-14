import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in range(gcd(a, b)):
  print('1', end='')
