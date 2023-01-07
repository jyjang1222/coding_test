# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    if n == 0:
        return 1
    mi = 0
    c = 0
    total = 0
    save = 0
    while True:           
        if total < n:
            total += c
            c += 1     
        elif total > n:
            total -= mi
            mi += 1

        if total == n:
            save += 1
            total += c
            c += 1     
            
        if c >= n: 
            save += 1         
            break

    return save
n = 15
r = solution(n)
print(r)