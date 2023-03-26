import sys

input = sys.stdin.readline


n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort(reverse=True)

print(lst[m-1])
