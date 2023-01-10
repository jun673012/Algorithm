import sys

input = sys.stdin.readline

p = int(input())

for i in range(9):
    p -= int(input())

print(p)
