import sys

input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

lst = list(sorted(set(x)))

dic = {}
for i in range(len(lst)):
  dic[lst[i]] = i

for i in x:
  print(dic[i], end=" ")
