#pypy3

import sys

input = sys.stdin.readline

s = input()
lst = [[0]*26 for __ in range(len(s))]

for i in range(len(s)):
  for j in range(26):
    if ord(s[i])-97 == j:
      lst[i][j] = lst[i-1][j]+1
    else:
      lst[i][j] = lst[i-1][j]
      
for __ in range(int(input())):
  q, l, r = input().split()
  if int(l) == 0: 
    print(lst[int(r)][ord(q)-97])
  else:
    print(lst[int(r)][ord(q)-97]-lst[int(l)-1][ord(q)-97])
