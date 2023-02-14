def solution(money):
    count = money // 5500
    spare = money % 5500
    answer = [count, spare]
    return answer