def solution(x):
    answer = False
    
    tmp = x
    h = 0
    for i in range(len(str(x))):
        h += x%10
        x //= 10

    if tmp % h == 0:
        answer = True
            
    return answer

