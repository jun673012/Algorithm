import sys

input = sys.stdin.readline

n = list(map(int, str(input().rstrip())))

n.sort(reverse=True)

for i in n:
    print(i,end='')
