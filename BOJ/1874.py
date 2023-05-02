import sys

input = sys.stdin.readline

n = int(input())
l = []
lst = []
tmp = 1
f = True
for i in range(n):
  s = int(input())
  while tmp <= s:
    l.append(tmp)
    lst.append("+")
    tmp += 1
  if l[-1] == s:
    l.pop()
    lst.append("-")
  else:
    f = False 
if f:
  print(*lst, sep="\n")
else:
  print("NO")
  

  
