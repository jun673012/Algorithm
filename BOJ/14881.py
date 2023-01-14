import sys

input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def exp(a, b, c):
  if c > a and c > b:
    return False
  return True if c % gcd(a, b) == 0 else False;

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
  
    if exp(a, b, c):
        print("YES")
    else:
        print("NO")
