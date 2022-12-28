import sys

input = sys.stdin.readline

a = int(input())
N = []
cnt = 0

for _ in range(a):
    N.append(int(input()))
if (a == 1):
    print(0)
else:
    dasom = N[0]
    No = sorted(N[1:], reverse=True)
    while (dasom <= No[0]):
        dasom += 1
        No[0] -= 1
        cnt += 1
        No.sort(reverse=True)
    print(cnt)
