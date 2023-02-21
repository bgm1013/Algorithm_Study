def solution(my_string):
    answer = []
    for i in range(len(my_string)):
        try:
            tmp = int(my_string[i])
            answer.append(tmp)
        except:
            pass 
    answer.sort()
    return answer