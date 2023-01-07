
# https://school.programmers.co.kr/learn/courses/30/lessons/70129


def changeBinary(num):
    #print(num)
    a = 1
    while True:
        if a >= num:
            break
        a *= 2

    st = ""
    while True:
        st += str(num // a)    
        num = num % a
        a //= 2
        if a == 0:
            break
    st = int(st)
    st = str(st)
    return st
    pass
def solution(s):
    count = 0
    i = 1
    while True:
        for v in s:
            if v == "0":
                count += 1

        s = s.replace("0" , "")
        #print(count, s)

        s = changeBinary(len(s))
        #print(s)
        if s == "1":
            break
        i += 1
    return [i, count]

s = "110010101001"

r = solution(s)
print(r)

"""
이진법 변환을 한다.
"""