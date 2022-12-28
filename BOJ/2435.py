import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = []

for i in range(n - k + 1):
    tmp = 0
    for j in range(i, i + k):
        tmp += arr[j]
    res.append(tmp)
print(max(res))
