# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def changeNum(n , tm):
    b = 1
    while True:
        if b >= tm:
            break
        b *= n
    a = ""
    while True:
        val = tm // b
        sample = "ABCDEF"
        if val >= 10:
            val = sample[val - 10]
        val = str(val)
        a += val
        tm = tm % b
        b //= n
        if b == 0:
            break
    if a[0] == "0":
        a = a[1:]
    a = str(a)
    return a
def solution(n, t, m, p):
    answer = ''
    a = "0"
    i = 1
    while True:
        a += changeNum(n , i)
        #print(a)
        if len(a) >= t*m: 
            break
        i += 1   
    #print(a)
    
    c = 0
    for i in range(len(a)):  
        if i % m + 1 == p:
            answer += a[i]
            c += 1
        if c == t:
            break
    return answer
n = 16
t = 16
m = 2
p = 1
r = solution(n , t , m , p)
print(r)
