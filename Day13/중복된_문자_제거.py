def solution(my_string):
    tmp = []
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] not in tmp:
            tmp.append(my_string[i])
            answer += my_string[i]
    return answer