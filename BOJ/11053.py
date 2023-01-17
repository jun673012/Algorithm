import sys

input = sys.stdin.readline

a = int(input())
array = list(map(int, input().split()))

dp = [1] * a

for i in range(1, a):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

result = max(dp)
print(result)
