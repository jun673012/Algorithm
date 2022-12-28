import sys

input = sys.stdin.readline

n = []
for _ in range(5):
  n.append(int(input()))

avg = sum(n) // 5
n.sort()

m = int(len(n) / 2)
mid = n[m]

print(avg)
print(mid)
