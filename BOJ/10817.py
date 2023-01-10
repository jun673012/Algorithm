import sys

input = sys.stdin.readline

n = list(map(int, input().split()))

print(sorted(n, reverse=True)[1])
