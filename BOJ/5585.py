import sys

input = sys.stdin.readline

n = int(input())

cnt = 0
ch = 1000 - n

while ch != 0:
  cnt += 1
  if ch - 500 >= 0:
    ch -= 500
  elif ch - 100 >= 0:
    ch -= 100
  elif ch - 50 >= 0:
    ch -= 50
  elif ch - 10 >= 0:
    ch -= 10
  elif ch - 5 >= 0:
    ch -= 5
  elif ch - 1 >= 0:
    ch -= 1
    
print(cnt)
