def solution(balls, share):
    up = factorial(balls)
    down1 = factorial(balls-share)
    down2 = factorial(share)
    answer = up/(down1*down2)
    return answer

def factorial(n):
    return_value = 1
    for value in range(1, n+1):
        return_value *= value
    return return_value 