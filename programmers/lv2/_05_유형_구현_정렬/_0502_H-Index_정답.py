# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort()
    citations.reverse()
    #print(citations)
    mx = len(citations)
    for i in range(len(citations)):
        
        c = 0
        for j in range(mx):
            if citations[j] >= mx:
                c += 1
        #print(c , " " , mx)
        if c >= mx:
            return mx
        mx -= 1             
    return answer

citations = [3, 0, 6, 1, 5]	

r = solution(citations)
print(r)