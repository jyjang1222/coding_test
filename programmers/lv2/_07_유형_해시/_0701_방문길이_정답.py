# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def checkMove(y , x):
    if y < -5 or x < -5 or y > 5 or x > 5:
        return False
    return True 

def solution(dirs):
    x = 0
    y = 0
    myset = set()
    for i in range(len(dirs)):
        #print(myset)
        s = dirs[i]
        if s == "U":
            ny = y + 1
            nx = x 
            if checkMove(ny, nx):
                st = str(y) + str(x) + str(ny) + str(nx)
                myset.add(st)
                st = str(ny) + str(nx) + str(y) + str(x)
                myset.add(st)
                x = nx
                y = ny
        elif s == "D":
            ny = y - 1
            nx = x 
            if checkMove(ny, nx):
                st = str(y) + str(x) + str(ny) + str(nx)
                myset.add(st)
                st = str(ny) + str(nx) + str(y) + str(x)
                myset.add(st)
                x = nx
                y = ny
        elif s == "L":
            ny = y 
            nx = x - 1
            if checkMove(ny, nx):
                st = str(y) + str(x) + str(ny) + str(nx)
                myset.add(st)
                st = str(ny) + str(nx) + str(y) + str(x)
                myset.add(st)
                x = nx
                y = ny
        elif s == "R":
            ny = y
            nx = x + 1
            if checkMove(ny, nx):
                st = str(y) + str(x) + str(ny) + str(nx)
                myset.add(st)
                st = str(ny) + str(nx) + str(y) + str(x)
                myset.add(st)
                x = nx
                y = ny
    answer = len(myset) // 2
    return answer
dirs = "ULURRDLLU"
r = solution(dirs)
print(r)