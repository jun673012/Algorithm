import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
  a.append(int(input()))
  
a.sort()
cnt = Counter(a)
c = cnt.most_common()

print(round(sum(a)/n))
print(a[n//2])

if len(c) > 1:
  if c[0][1] == c[1][1]:
    print(c[1][0])
  else:
    print(c[0][0])
else:
  print(c[0][0])
  
print(a[-1]-a[0])
