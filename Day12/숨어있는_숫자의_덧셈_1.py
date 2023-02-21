def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        try:
            tmp = int(my_string[i])
            answer += tmp
        except:
            pass 
    return answer