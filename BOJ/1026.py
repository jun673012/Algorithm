import sys

input = sys.stdin.readline

res = 0

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(N):
  res += A[i] * B[i]

print(res)
