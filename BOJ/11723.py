import sys

input = sys.stdin.readline

m = int(input())

res = 0
for i in range(m):
  c = input().split()

  if c[0] == 'all':
    res = (1 << 20) - 1
  elif c[0] == 'empty':
    res = 0
  else:
    op = c[0]
    n = int(c[1]) - 1

    if op == 'add':
        res |= (1 << n)
    elif op == 'remove':
        res &= ~(1 << n)
    elif op == 'check':
        if res & (1 << n) == 0:
            print(0)
        else:
            print(1)

    elif op == 'toggle':
        res = res ^ (1 << n)
