import sys
import math

input = sys.stdin.readline

n = int(input())

for _ in range(n):
  res = []
  m = list(map(int, input().split()))
  
  for i in range(len(m) - 1):
    for j in range(i + 1, len(m)):
      res.append(math.gcd(m[i], m[j]))
      
  print(max(res))    
