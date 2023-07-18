def solution(s1, s2):
    answer = 0
    for tmp in s1:
        find_count = s2.count(tmp)
        if find_count > 0:
            answer += 1
    return answer