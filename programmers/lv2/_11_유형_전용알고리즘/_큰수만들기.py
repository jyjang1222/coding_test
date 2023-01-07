
def getCombi(num , k):
    
    di = {"arr" : "" ,  "d" : 0}
    stack = [di]
    combiList = []
    size = len(num)
    while len(stack) > 0:
        pop = stack.pop()
        arr = pop["arr"]
        d = pop["d"]
        
        if len(arr) == size - k:
            combiList.append(arr)
            continue
        if d == size:
            continue
        temparr = arr
        temparr += num[d]
        di = {"arr" : temparr , "d" : d + 1}            
        stack.append(di)           
        temparr =arr
        di = {"arr" : temparr , "d" : d + 1}
        stack.append(di)      
        pass
    return combiList
    pass
def solution(number, k):
    answer = ''
    mx = max(getCombi(number , k))    
    return mx
number , k = "1924" , 2
number , k = "1231234" , 3
r = solution(number , k)
print(r)