def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    res = 45 - answer
    return res
