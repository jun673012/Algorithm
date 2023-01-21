import sys
input = sys.stdin.readline

n = int(input())

f = [0] * 1000001
f[1] = f[2] = 1

for i in range(3, n + 1):
    f[i] = (f[i - 1] + f[i - 2]) % 1000000007

print(f[n])
