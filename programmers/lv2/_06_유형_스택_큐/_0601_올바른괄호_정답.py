# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    l = 0
    for i in range(len(s)):
        if l < 0:
            return False
        if s[i] == "(":
            l += 1
        elif(s[i] == ")"):
            l -= 1
    if l != 0:
        return False

    return True


s = "()()"
r = solution(s)
print(r)