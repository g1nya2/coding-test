def solution(my_string, n):
    answer = ''
    for x in my_string:
        for i in range(n):
            answer+=x
    return answer