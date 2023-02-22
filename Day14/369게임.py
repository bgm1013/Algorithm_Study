def solution(order):
    str_order = str(order)
    count_3 = str_order.count('3')
    count_6 = str_order.count('6')
    count_9 = str_order.count('9')
    answer = count_3+count_6+count_9
    return answer