# https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    #print(s)
    s = s[2:]
    #print(s)
    s = s[:-2]
    #print(s)
    token = s.split("},{")
    #print(token)
    token.sort(key=len)
    #print(token)
    for i in range(len(token)):
        token2 = token[i].split(",")
        for j in range(len(token2)):
            a = token2[j]
            if a not in answer:
                answer.append(a)
                break
    
    for i in range(len(answer)):
        answer[i] = int(answer[i])
    
    return answer


s = "{{20,111},{111}}"
r = solution(s)
print(r)