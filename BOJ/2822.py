import sys

input = sys.stdin.readline

a = []
b = []
res = 0

for _ in range(8):
  a.append(int(input()))
  
for _ in range(5):
  b.append(a.index(max(a)) + 1)
  res += a[a.index(max(a))]
  a[a.index(max(a))] = 0
  
b.sort()
  
print(res)

for i in b:
  print(i, end=' ')
