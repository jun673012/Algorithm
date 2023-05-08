import math

def lcm(a,b):
    return (a * b) // math.gcd(a,b)

def solution(n, m):
    answer = [math.gcd(n, m), lcm(n, m)]
    return answer
