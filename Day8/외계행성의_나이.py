def solution(age):
    str_age = str(age)
    answer = ''
    for i in range(len(str_age)):
        answer += chr(int(str_age[i])+97)
    return answer