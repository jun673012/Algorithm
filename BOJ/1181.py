import sys

input = sys.stdin.readline

a = []
n = int(input())
for i in range(n):
  a.append(input().rstrip())

a = list(set(a))
a.sort()
a.sort(key=len)

print(*a, sep='\n')
