import sys

input = sys.stdin.readline

while True:
  try:
    n = int(input())
  except:
        break
  o = 0
  res = 1
  while True:
    o = o*10 + 1
    if o%n == 0:
      print(res)
      break
    res += 1
