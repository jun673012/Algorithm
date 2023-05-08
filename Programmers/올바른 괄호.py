def solution(s):
    answer = False
    a = list(s)
    b = []
    for i in a:
        b.append(i)
        if i == ')' and len(b) == 1:
            break
        if i == ')' and b[-2] == '(':
            b.pop()
            b.pop()
    else:
        if len(b) == 0:
            answer = True
    return answer
