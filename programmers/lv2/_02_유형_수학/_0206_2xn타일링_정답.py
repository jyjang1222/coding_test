# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    if n <= 2:
        return n

    a = 0
    b = 1
    c = a + b
    for i in range(2, n + 1):
        a = b
        b = c
        c = a + b 
    
    return c % 1000000007

n = 4
r = solution(n)
print(r)

"""
피보나치 수열

"""