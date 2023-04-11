import sys
import math
input = sys.stdin.readline

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

aa = a1*b2 + a2*b1
cc = a2*b2
e = math.gcd(aa, cc)

print(aa//e, cc//e)
