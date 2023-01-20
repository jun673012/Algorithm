import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

for i in sorted(list(set(num))):
  print(i, end=' ')
