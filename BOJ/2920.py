import sys

input = sys.stdin.readline

t = list(map(int, input().split()))

ant = dnt = 0

for i in range(7):
  if t[i + 1] == t[i] + 1:
      ant += 1
  elif t[i] == t[i + 1] + 1:
      dnt += 1

if ant == 7:
  print("ascending")
elif dnt == 7:
  print("descending")
else:
  print("mixed")
  
