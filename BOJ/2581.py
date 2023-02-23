import sys

input = sys.stdin.readline

m = int(input())
n = int(input())
res = []

for num in range(m, n + 1):
    count = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                count += 1
                break
        if count == 0:
            res.append(num)

      
if len(res) < 1:
  print(-1)
else:
  print(sum(res))
  print(min(res))
  
