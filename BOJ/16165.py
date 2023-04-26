import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}

for i in range(n):
  g = input().rstrip()
  lst = []
  c = int(input())
  
  for _ in range(c):
    lst.append(input().rstrip())
  dic[g] = lst

for i in range(m):
  q = input().rstrip()
  qt = int(input())
  
  if qt == 0:
    a = dic.get(q)
    a.sort()
    print(*a, sep="\n")
  else:
    b = [k for k, v in dic.items() for j in v if j == q]
    print(*b)
