def solution(hp):
    big_ant = hp//5
    left_ant = hp%5
    mid_ant = left_ant//3
    small_ant = left_ant%3
    answer = big_ant+mid_ant+small_ant
    return answer