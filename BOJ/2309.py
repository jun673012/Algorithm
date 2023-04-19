import sys

input = sys.stdin.readline

n = []
for i in range(9):
  n.append(int(input()))
n.sort()
tmp = sum(n)
for i in range(len(n)-1):
  for j in range(i+1, len(n)):
    if tmp-(n[i]+n[j]) == 100:
      n.remove(n[i])
      n.remove(n[j-1])
      break
  if len(n) == 7:
    break

print(*n, sep="\n")
