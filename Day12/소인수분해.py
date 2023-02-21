def solution(n):
    tmp = []
    division = 2               
    while division <= n:
        if n % division == 0:   
            n = n / division  
            tmp.append(division)  
        else:
            division = division + 1   
    answer = list(set(tmp))
    answer.sort()
    return answer