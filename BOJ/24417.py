import sys

input = sys.stdin.readline

n = int(input())

a, b = 1, 1

for _ in range(n - 2):
    b, a = (a + b) % 1000000007, b
  
print(b, n - 2)
