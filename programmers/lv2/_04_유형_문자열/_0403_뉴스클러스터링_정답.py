
# https://school.programmers.co.kr/learn/courses/30/lessons/17677
def getArr(str):
    sample = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    arr = []
    for i in range(len(str) - 1):
        a = str[i].upper()
        if a not in sample:
            continue
        b = str[i+1].upper()
        if b not in sample:
            continue
        c = a + b
        arr.append(c)        
    return arr
def solution(str1, str2):  
    arr1 = getArr(str1)
    arr2 = getArr(str2)
    if len(arr1) == 0 and len(arr2) == 0:
        return 65536
    c1 = 0
    c2 = len(arr1) + len(arr2)
    for v in arr1:
        if v in arr2:
            index = arr2.index(v)
            print(v)
            del(arr2[index])
            c1 += 1 
    #print(c1 , " " , c2)
    c2 = c2 - c1
    #print(c1 , " " , c2)
    
    r = c1 / c2 * 65536
    r = int(r)

    return r

str1 = "FRANCE"
str2 = "french"

r = solution(str1 , str2)
print(r)