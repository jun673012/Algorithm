import sys

input = sys.stdin.readline

n = list(map(int, input().split()))
cnt = 0

for i in range(len(n) - 1):
  if n[i] <= n[i + 1]:
    cnt += 1
    
if cnt == len(n) - 1:
  print("Good")
else:
  print("Bad")
