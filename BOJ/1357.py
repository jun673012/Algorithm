import sys

input = sys.stdin.readline

x, y = map(int, input().split())

x, y = str(x)[::-1], str(y)[::-1]
c = int(x) + int(y)

print(int(str(c)[::-1]))
