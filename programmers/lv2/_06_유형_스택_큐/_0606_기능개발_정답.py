# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(p, s):
    arr = []
    count = 0
    while True:
        # 판정
        temp = []
        for i in range(count, len(p)):
            if p[i] == 100:
                temp.append(p[i])
                count += 1
            else:
                break
        if len(temp) > 0:
            arr.append(len(temp))
        # 증가 
        for i in range(count, len(p)):
            p[i] += s[i]
            if p[i] >= 100:
                p[i] = 100
        if count >= len(p):
            break
        pass
    return arr

p = [93,30,50]
s = [1,30,5]
r = solution(p, s)
print(r)
