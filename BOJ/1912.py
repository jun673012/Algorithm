import sys

input = sys.stdin.readline

n = int(input())
nn = list(map(int, input().split()))

for i in range(1, n):
  nn[i] = max(nn[i], nn[i] + nn[i-1])
  
print(max(nn))
