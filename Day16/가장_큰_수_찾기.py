def solution(array):
    max_value = max(array)
    for i, value in enumerate(array):
        if value == max_value:
            return_index = i
    answer = [max_value, return_index]
    return answer