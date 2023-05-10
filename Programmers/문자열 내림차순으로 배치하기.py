def solution(s):
    answer = ''
    a = list(s)
    a.sort(reverse=True)
    for i in a:
        answer += i
    return answer
