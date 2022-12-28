import sys

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

maxA = max(A)
minA = min(A)

res = maxA * minA

print(res)
