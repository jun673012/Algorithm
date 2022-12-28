N, K = map(int, input().split())
dp = [0 for _ in range(K+1)]

for _ in range(N):
  W, V = map(int, input().split())
  for i in range(K, W-1, -1):
    dp[i] = max(dp[i], dp[i-W] + V)

print(dp[-1])
