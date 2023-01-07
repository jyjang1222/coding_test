# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def printMap(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j] , end=" ")
        print()
    print("-----------------------------")
def checkMap(m , n , board):
    temp = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if rectCheck(i , j , board):
                temp[i][j] = 1
                temp[i][j + 1] = 1
                temp[i + 1][j] = 1
                temp[i + 1][j + 1] = 1
    #printMap(temp)
    c = 0
    for i in range(m):
        for j in range(n):
            if temp[i][j] == 1:
                board[i][j] = '#'
                c += 1
    return c
    pass
def downMap(board):
    for i in range(len(board[0])):
        lastindex = len(board) - 1
        swapindex = len(board) - 1
        for j in range(len(board)):
            if board[lastindex][i] != '#':
                temp = board[lastindex][i]
                board[lastindex][i] = board[swapindex][i]
                board[swapindex][i] = temp
                swapindex -= 1         
            lastindex -= 1
    pass

def rectCheck(y , x , board):
    a = board[y][x]
    if a == '#':
        return False
    for i in range(2):
        for j in range(2):
            y2 = y + i
            x2 = x + j
            if y2 < 0 or x2 < 0 or y2 >= len(board) or x2 >= len(board[0]):
                return False
            if board[y2][x2] != a:
                return False
    return True
            

def changeMap(m,n,board):
    temp = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):           
            temp[i][j] = board[i][j]
    return temp

def solution(m, n, board):
    answer = 0
    board = changeMap(m,n,board)
    #printMap(board)
    while True:
        c = checkMap(m, n , board) 
        if c == 0:
            break
        answer += c
        #printMap(board)
        downMap(board)
        #printMap(board)
    return answer


#m ,n, board = 6, 6 , 	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

m = 4 
n = 4 
board =  ["CCBDE", "AAADE", "AAABF", "CCBBF"]
m , n , board =  2, 3, ["AAA", "AAA"]
r = solution(m, n , board)
print(r)