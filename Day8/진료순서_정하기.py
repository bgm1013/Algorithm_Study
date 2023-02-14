def solution(emergency):
    tmp = [value for value in emergency]
    emergency.sort(reverse = True)
    tmp_dict = dict()
    for i, value in enumerate(emergency):
        tmp_dict[value] = i+1
    sorted_dict = dict(sorted(tmp_dict.items()))
    answer = []
    for value in tmp:
        answer.append(sorted_dict[value])
    return answer