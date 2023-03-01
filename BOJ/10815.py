import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
aa = list(map(int, input().split()))
a.sort()
res = []

for i in aa:
  left = 0 
  right = n-1
  f = False

  while left<=right:
      mid = (left+right)//2
      if a[mid] == i:
          res.append(1)
          f = True
          break
      elif a[mid] > i:
          right = mid-1
      else :
          left = mid+1
        
  if not f:
    res.append(0)

print(*res)
