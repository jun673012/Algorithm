import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  s1 = set(map(int, input().split()))
  m = int(input())
  s2 = list(map(int, input().split()))
  
  for i in s2:
    if i in s1:
      print(1)
    else:
      print(0)
  
    
