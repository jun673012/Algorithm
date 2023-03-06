import sys

input = sys.stdin.readline

a, b = map(int, input().split())

ae = set(input().split())
be = set(input().split())

print(len(ae-be)+len(be-ae))
