def solution(numbers, direction):
    answer = []
    if direction=="left":
        for x in numbers[1:]:
            answer.append(x)
        answer.append(numbers[0])
    else:
        answer.append(numbers[-1])
        for x in numbers[:-1]:
            answer.append(x)
    return answer