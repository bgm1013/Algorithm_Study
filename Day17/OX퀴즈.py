def solution(quiz):
    answer = []
    for qz in quiz:
        tmp = qz.split()
        if tmp[1] == '+':
            left = int(tmp[0])+int(tmp[2])
        else:
            left = int(tmp[0])-int(tmp[2])
        if left == int(tmp[4]):
            answer.append('O')
        else:
            answer.append('X')
    return answer