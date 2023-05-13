import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    res = pow(a, b, 10)
    print(res if res != 0 else 10)
