import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r, s = input().split()

    for i in s:
        print(int(r) * i, end='')
    print()
