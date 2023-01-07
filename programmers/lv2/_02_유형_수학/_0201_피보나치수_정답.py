# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    a = 0
    b = 1
    c = a + b
    for i in range(2, n):
        a = b        
        b = c
        c = b + a
    return c % 1234567
n = 5
r = solution(n)
print(r)

"""
피보나치 수열이다. 
F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
"""