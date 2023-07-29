import sys
import heapq

input = sys.stdin.readline

n = int(input())

lh = []
rh = []

for i in range(n):
    num = int(input())
    if len(lh) == len(rh):
        heapq.heappush(lh, -num)
    else:
        heapq.heappush(rh, num)
    if rh and rh[0] < -lh[0]:
        l = heapq.heappop(lh)
        r = heapq.heappop(rh)

        heapq.heappush(lh, -r)
        heapq.heappush(rh, -l)

    print(-lh[0])
