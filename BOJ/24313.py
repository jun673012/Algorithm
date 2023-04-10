import sys

input = sys.stdin.readline

a1, a2 = map(int, input().split())
c = int(input())
n = int(input())

print(1) if a1*n+a2 <= c*n and c >= a1 else print(0)
