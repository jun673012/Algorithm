def solution(sizes):
    answer = 0
    a = 0
    b = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if sizes[i][0] > a:
            a = sizes[i][0]
        if sizes[i][1] > b:
            b = sizes[i][1]
    answer = a*b
    return answer
