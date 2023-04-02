import sys

input = sys.stdin.readline

arr = [0]*2 + [1]*(123456*2)

for i in range(2, 123456*2+1):
    if arr[i]:
        for j in range(i*2, 123456*2+1, i):
            arr[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(arr[n+1:n*2+1]))
