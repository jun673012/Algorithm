import sys

input = sys.stdin.readline

n = int(input())

d = [0] * 1500000
d[1] = 1

for i in range(2, 1500000):
    d[i] = (d[i - 1] + d[i - 2]) % 1000000

print(d[n %  1500000])
