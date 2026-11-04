def solution(s1, s2):
    answer = 0
    if len(s1)>len(s2):
        for x in s1:
            for z in s2:
                if x==z:
                    answer+=1
                else:
                    continue
    else:
        for x in s2:
            for z in s1:
                if x==z:
                    answer+=1
                else:
                    continue
    
    return answer