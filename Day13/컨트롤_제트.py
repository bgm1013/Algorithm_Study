def solution(s):
    tmp = []
    for num in s.split():
        try:
            tmp.append(int(num))
        except:
            if tmp:
                tmp.pop()
    answer = sum(tmp)
    return answer