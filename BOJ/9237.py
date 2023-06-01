import sys

input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
t.sort(reverse=True)

for i in range(len(t)):
  t[i] = t[i]+i+1
  
print(max(t)+1)
