import sys

input = sys.stdin.readline

lst = [0 for _ in range(10001)]
lst[1] = 1
for i in range(2, 98):
  for j in range(i * 2, 10001, i):
    lst[j] = 1
      
t = int(input())
for i in range(t):
  a = int(input())
  b = a // 2
  for j in range(b, 1, -1):
    if lst[a-j] == 0 and lst[j] == 0:
      print(j, a-j)
      break
