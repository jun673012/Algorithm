import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
l = [0]
for i in range(n):
  l.append(l[i] + lst[i]) 
m = int(input())
for _ in range(m):
  i, j = map(int, input().split())
  print(l[j]-l[i-1])
