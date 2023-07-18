def solution(my_string):
    tmp_list = my_string.split(' ')
    answer = int(tmp_list[0])
    for i in range(1, len(tmp_list), 2):
        print(tmp_list[i])
        if tmp_list[i] == '+':
            answer = answer+int(tmp_list[i+1]) 
        elif tmp_list[i] == '-':
            answer = answer-int(tmp_list[i+1]) 
    return answer