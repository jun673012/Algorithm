import sys

input = sys.stdin.readline

s = input().rstrip()
a = set()

for i in range(len(s)):
  for j in range(i, len(s)):
    a.add(s[i:j+1])

print(len(a))
