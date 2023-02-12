import sys

input = sys.stdin.readline

n, d = map(int, input().split())

cnt = 0

for i in range(1, n + 1):
    cnt += str(i).count(str(d))
      
print(cnt)
