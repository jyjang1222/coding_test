def solution(n, k):
    arr = [i + 1 for i in range(n)]
    answer = []
    di = {"arr" : arr , "d" : 0}
    stack = [di]
    while True:
        if len(stack) == 0:
            break
        pop = stack.pop(0)
        arr = pop["arr"]
        d = pop["d"]
        if d == len(arr):
            if k == 0:
                return arr
            k -= 1
            continue
        
        for i in range(d, len(arr)):
            temparr = arr.copy()
            temp = temparr[i]
            temparr[i] = temparr[d]
            temparr[d] = temp
            di = {"arr" : temparr , "d" : d + 1}
            stack.append(di)
    return []

n = 3
k = 5
r = solution(n, k)
print(r)