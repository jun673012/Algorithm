import sys

input = sys.stdin.readline

tmp = []
res = 0

for _ in range(10):
    tmp.append(int(input()))

for i in tmp:
    res += i
    if res >= 100:
        if res - 100 > 100 - (res - i):
            res -= i
            break
print(res)
