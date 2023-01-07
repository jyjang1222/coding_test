# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def changeBinary(n):
    a = 1
    while True:
        if a >= n:
            break
        a *= 2
    #print(a)
    st = ""
    while True:
        temp = n // a
        st += str(temp)
        n = n % a
        a //= 2

        if a == 0:
            break
    #print(st)
    return st

def count1(st):
    c = 0
    for v in st:
        if v == "1":
            c += 1
    return c 

def solution(n):
    st = changeBinary(n)
    c1 = count1(st)
    n += 1
    while True:
        st = changeBinary(n)
        c2 = count1(st)
        if c1 == c2:
            break
        n += 1
    return n
    
n = 15
r = solution(n)
print(r)




"""
이진법 변환을 한다.

"""