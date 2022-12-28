import sys

input = sys.stdin.readline

x, y, w, h = list(map(int, input().split()))

resX = min(w - x, x - 0)
resY = min(h - y, y - 0)

print(min(resX, resY))
