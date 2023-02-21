def solution(sides):
    bool_1 = sides[0]+sides[1] > sides[2]
    bool_2 = sides[1]+sides[2] > sides[0]
    bool_3 = sides[2]+sides[0] > sides[1]
    answer_bool = bool_1 & bool_2 & bool_3
    if answer_bool:
        answer = 1
    else:
        answer = 2
    return answer