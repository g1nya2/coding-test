def solution(s):
    answer = True
    if not len(s)==4 and not len(s)==6:
        return False
    for x in s:
        if x.isdigit()!=1:
            return False  
    return answer