def solution(n):
    n = list(str(n))
    answer = int(''.join(sorted(n, reverse=True)))
    return answer
