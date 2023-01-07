# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(p):
    answer = []
    for i in range(len(p)):
        c = 0
        for j in range(i + 1, len(p)):
            if p[i] <= p[j]:
                c += 1
            else:
                c += 1
                break
                
        answer.append(c)
    return answer


prices = [1,2,3,2,3]

r = solution(prices)

print(r)