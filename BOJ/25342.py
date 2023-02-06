import sys
import math
#python -v 3.9↑ be available lcm
input = sys.stdin.readline

t = int(input())
  
for _ in range(t):
  n = int(input())
  print(max(math.lcm(n - 3, n - 2, n - 1), math.lcm(n - 3, n - 1, n), math.lcm(n - 2, n - 1, n)))
