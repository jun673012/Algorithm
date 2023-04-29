import sys

input = sys.stdin.readline

lst = list(input().rstrip())
l = []
n = int(input())
for _ in range(n):
  e = list(input().rstrip().split())
  if e[0] == "P":
    lst.append(e[1])
  elif e[0] == "L":
    if lst:
      l.append(lst.pop())
  elif e[0] == "D":
    if l:
      lst.append(l.pop())
  elif e[0] == "B":
    if lst:
      lst.pop()
      
lst.extend(reversed(l))
print(*lst, sep="")
