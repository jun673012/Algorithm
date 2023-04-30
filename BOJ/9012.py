import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  lst = list(input().rstrip())
  lst2 = []
  for i in range(len(lst)):
    lst2.append(lst.pop())
    if lst2[len(lst2)-1] == "(" and lst2[len(lst2)-2] == ")":
      lst2.pop()
      lst2.pop()
  print("YES" if not lst2 else "NO")
  

