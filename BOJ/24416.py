import sys

input = sys.stdin.readline

t = int(input())

f = [1 for i in range(t + 1)]


def fib(n):  
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    f[1] = 1
    f[2] = 1
    cnt = 1
  
    for i in range(3, n):
        f[i] = f[i - 1] + f[i - 2]
        cnt += 1
    return cnt


print(fib(t), fibonacci(t))
