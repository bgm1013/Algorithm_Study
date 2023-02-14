def solution(n, k):
    answer = n * 12000
    service = n // 10
    drink = (k-service)*2000
    answer += drink
    return answer