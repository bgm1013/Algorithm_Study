def solution(array):
    answer = -1
    count_dict = dict()
    for value in array:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 0
    sorted_dict = sorted(count_dict.items(), key = lambda item:item[1], reverse = True)
    if len(sorted_dict) > 1 and sorted_dict[0][1] != sorted_dict[1][1] or len(sorted_dict) ==1:
        answer = sorted_dict[0][0]
    return answer