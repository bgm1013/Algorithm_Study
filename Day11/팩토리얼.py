def solution(n):
    i = 0
    while True:
        i += 1
        fac_value = factorial(i)
        if fac_value > n:
            break
    answer = i-1
    return answer

def factorial(n):
    return_value = 1
    for value in range(1, n+1):
        return_value *= value
    return return_value 