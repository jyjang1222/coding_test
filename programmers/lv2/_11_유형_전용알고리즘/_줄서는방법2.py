import math

def solution(n, k):
    answer = []
    numberList = [i for i in range(1, n+1)]
    k -= 1;
    
    
    while (n != 0):
        print("F " , math.factorial(n-1))
        temp = math.factorial(n-1) # 한개에 몇개씩의 값이 있을지 알 수 잇음.
        index = 0     
        print(k , temp , index , n)
        index = k // temp
        k = k % temp
        answer.append(numberList.pop(index))
        n -= 1
    
    return answer

n = 3
k = 5
r = solution(n, k)
print(r)