def solution(s):
    answer = ''
    num=0
    for x in s:
        if x==" ":
            num=0
            answer+=" "
            continue
        else:
            if not num%2:
                answer+=x.upper()
                num+=1
            else:
                answer+=x.lower()
                num+=1
    return answer