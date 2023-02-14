def solution(array):
    array.sort()
    median_pos = len(array)//2
    answer = array[median_pos]
    return answer