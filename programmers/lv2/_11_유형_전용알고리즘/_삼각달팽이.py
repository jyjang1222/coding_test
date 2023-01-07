
def solution(n):
    answer = []
    for i in range(n):
        arr = [0 for j in range(i + 1)]
        answer.append(arr)
    #print(answer)
    y = 0
    x = 0
    dir = "d" # d r
    c = n - 1
    k = 1
    while True:
        #print(dir , y , x)
        answer[y][x] = k
        if n == 0:
            break
        if dir == "d":
            if c == 0:
                dir = "r"
                n -= 1
                c = n
            else:
                k += 1
                y += 1
                c -= 1
        elif dir == "u":  
            if c == 0:
                dir = "d"
                n -= 1
                c = n
            else:
                k += 1
                x -= 1
                y -= 1
                c -= 1
        elif dir == "r":      
            if c == 0:
                dir = "u"
                n -= 1
                c = n
            else:
                k += 1
                x += 1
                c -= 1
            pass
    temp = []
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            temp.append(answer[i][j])
    return temp


n = 4
result = solution(n)
print(result)