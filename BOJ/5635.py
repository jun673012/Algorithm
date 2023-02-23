import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
  name, dd, mm, yyyy = input().split()
  arr.append((int(yyyy), int(mm), int(dd), name))
  
arr.sort()

print(arr[-1][3])
print(arr[0][3])
