import sys

input = sys.stdin.readline

k = int(input())

for i in range(k):
    n = list(map(int, input().split()))
    m = n[0]
    gap = []
    n.remove(n[0])
    n.sort()
    for j in range(len(n) - 1):
        gap.append(n[j + 1] - n[j])

    print('Class', i + 1)
    print('Max', str(max(n)) + ',', 'Min', str(min(n)) + ',', 'Largest gap', max(gap))
