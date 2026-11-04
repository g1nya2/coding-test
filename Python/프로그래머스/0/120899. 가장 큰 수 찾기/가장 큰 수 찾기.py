def solution(array):
    answer = 0
    num=0
    answer=sorted(array,reverse=True)[0]
    for x in array:
        if x!=answer:
            num+=1
        else:
            break
            
    return [answer,num]