def solution(array, n):
    diff_list = []
    for arr in array:
        tmp = abs(arr-n)
        diff_list.append(tmp)
    min_diff = min(diff_list)
    count = diff_list.count(min_diff)
    if count == 1:
        answer = array[diff_list.index(min_diff)]
    else:
        tmp_list = []
        for i, dl in enumerate(diff_list):
            if dl == min_diff:
                tmp_list.append(array[i])
                answer = min(tmp_list)
    return answer