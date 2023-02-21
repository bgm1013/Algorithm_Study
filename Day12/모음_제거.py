def solution(my_string):
    answer = my_string.replace('a', '').replace('i', '').replace('e', '')
    answer = answer.replace('o', '').replace('u', '')
    return answer