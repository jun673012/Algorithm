import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

s.sort()

res = max(s) - min(s)


print(res)
