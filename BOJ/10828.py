import sys

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
  a = input().rstrip().split()
  if a[0] == "push":
    lst.append(a[1])
  elif a[0] == "pop":
    print(lst.pop() if lst else -1)
  elif a[0] == "size":
    print(len(lst))
  elif a[0] == "empty":
    print(0 if lst else 1)
  else:
    print(lst[-1] if lst else -1)
