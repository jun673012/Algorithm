import sys

input = sys.stdin.readline

n = int(input())

c = []
cnt = 0

for _ in range(n):
  c.append(int(input()))
  
for i in range(n-1, 0, -1):
  while True:
    if c[i-1] >= c[i]:
      c[i-1] -= 1
      cnt += 1
    else:
      break
    
print(cnt)
