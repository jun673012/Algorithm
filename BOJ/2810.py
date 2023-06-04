import sys

input = sys.stdin.readline

n = int(input())
s = list(input())
cnt = 0
tmp = 0
chk = False
for i in range(n):
  if s[i] == 'S':
    cnt += 1
  elif s[i] == 'L':
    chk = True
    tmp += 1
    if tmp == 2:
      cnt += 1
      tmp = 0
if chk == True:
  cnt += 1
      
print(cnt)
