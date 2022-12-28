import sys

input = sys.stdin.readline

n = []
s = [0 for _ in range(3)]

for i in range(3):
    n = list(map(int, input().split()))
    s[i] = sum(n)

for j in range(3):
    if s[j] == 0:
        print('D')
    elif s[j] == 1:
        print('C')
    elif s[j] == 2:
        print('B')
    elif s[j] == 3:
        print('A')
    else:
        print('E')
