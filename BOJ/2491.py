import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

cntb = [1] * n
cnts = [1] * n

for i in range(1, n):
  if num[i] >= num[i - 1]:
    cntb[i] = max(cntb[i], cntb[i - 1] + 1)    
  if num[i] <= num[i - 1]:
    cnts[i] = max(cnts[i], cnts[i - 1] + 1)
    
print(max(max(cntb), max(cnts)))
