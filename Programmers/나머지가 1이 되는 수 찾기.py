def solution(n):
    answer = []
    for i in range(1, n):
        if n % i == 1:
            answer.append(i)
    return min(answer)
