# https://school.programmers.co.kr/learn/courses/30/lessons/92335?language=python3

import math
def changeRadix(n , k):
    a = 1
    while True:
        if a >= n:
            break
        a *= k
    #print(a, n)
    st = ""
    while True:
        temp = n // a
        st += str(temp)
        n %= a
        a //= k
        if a == 0:
            break
    #print(st)
    st = int(st)
    st = str(st)
    return st

def checkPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    i = 2
    mx = int(math.sqrt(n))
    #print(n , mx)
    while i <= mx:
        if n % i == 0:
            return False
        i += 1
    return True
    
def solution(n, k):
    answer = -1
    st = changeRadix(n , k)
    arr = st.split("0")
    #print(arr)
    c = 0
    for v in arr:
        if v == '':
            continue
        if checkPrime(int(v)):
            c += 1
    return c

n = 110011
k = 10
r = solution(n , k)
print(r)


"""
3~10진수로 형변을 한다. 이후 소수 검사한다.

"""