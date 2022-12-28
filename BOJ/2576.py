import sys

input = sys.stdin.readline

n = []
res = []
cnt = 0

for _ in range(7):
    n.append(int(input()))

for i in range(7):
    if n[i] % 2 != 0:
        res.append(n[i])

if res == []:
    print('-1')
else:
    print(sum(res))
    print(min(res))
