import sys

input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
  name = list(input().split())
  dic[name[0]] = name[1]
  if name[1] == 'leave':
    del dic[name[0]]
dic = sorted(dic, reverse=True)

for i in dic:
  print(i)
