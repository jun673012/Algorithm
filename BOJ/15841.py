import sys

input = sys.stdin.readline

d = [0] * 490

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

k = int(input())

while k != -1:    
    print("Hour", str(k) + ":", fibo(k), "cow(s) affected")
    k = int(input())
  
