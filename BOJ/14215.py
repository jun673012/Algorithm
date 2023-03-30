import sys

input = sys.stdin.readline

b = list(map(int, input().split()))
b.sort()

print(sum(b) if b[0]+b[1] > b[2] else (b[0]+b[1])*2-1)
