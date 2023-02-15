def solution(box, n):
    tmp1 = int(box[0] //n) 
    tmp2 = int(box[1] // n)
    tmp3 = int(box[2] //n)
    answer = tmp1*tmp2*tmp3
    return answer