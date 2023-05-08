def solution(s):
    a = list(map(int, s.split()))
    answer = '{} {}'.format(min(a), max(a))
    
    return answer
