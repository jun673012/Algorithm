import sys

input = sys.stdin.readline

n = int(input())
dic = {}

for _ in range(n*2-1):
  a = input().rstrip()
  if a in dic:
    dic[a] += 1
  else:
    dic[a] = 0
for i in dic:
  if dic[i]%2 == 0:
    print(i)
    break
