# https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    di = {}
    for i in range(len(sample)):
        di[sample[i]] = (i + 1)
    lastnum = 27
    i = 1
    j = 0
    while True:
        if msg == "":
            break
        a = msg[:i]
        b = msg[:i + 1]
        if a == b:
            answer.append(di[a])
            break
        if b in di:
            i += 1
        else:
            answer.append(di[a])
            di[b] = lastnum
            lastnum += 1
            msg = msg[i:]
            i = 1
        j += 1
    # for i in range(len(answer)):
    #     answer[i] = di[answer[i]]
    #     pass
    return answer
msg = "TOBEORNOTTOBEORTOBEORNOT"
r = solution(msg)
print(r)