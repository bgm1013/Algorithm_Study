def solution(s):
    tmp = list(set(list(s)))
    answer_list = []
    for alphabet in tmp:
        if s.count(alphabet) == 1:
            answer_list.append(alphabet)
    answer_list.sort()
    answer = ''.join(answer_list)
    return answer