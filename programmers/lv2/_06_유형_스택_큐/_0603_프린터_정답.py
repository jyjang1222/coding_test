# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(p, l):
    c = 0
    while True:
        #print(l , " " , p)
        mx = max(p)
        if p[0] == mx:
            if l == 0:
                c += 1
                break
            del(p[0])
            c += 1
        else:        
            a = p[0]
            del(p[0])
            p.append(a)
        if l == 0:
            l = len(p)
        l -= 1
        
        
    return c
p = [1, 1, 2, 3, 2, 1]
l = 0
r = solution(p , l)
print(r)