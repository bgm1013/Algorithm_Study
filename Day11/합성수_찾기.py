def solution(n):
    tmp1 = []
    for i in range(1, n+1):
        tmp2 = []
        for j in range(1, i+1):
            if (i % j == 0) :
                tmp2.append(j)
        if len(tmp2) >= 3:
            tmp1.append(i)
    answer = len(tmp1)
    return answer