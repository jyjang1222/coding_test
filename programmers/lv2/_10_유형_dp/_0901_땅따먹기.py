# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = 0
    size= len(land)
    for i in range(size): 
        print()
        print(i , end=" ")
        for j in range(size):
            print(j , end=" ")
            for k in range(size):
                print(k , end=" ")
                for n in range(size):
                    print(n , end=" ")
    return answer

land = []
a = 0
for i in range(4):
    land.append([])
    for j in range((4)):
        land[i].append(a)
        a += 1
print(land)
r = solution(land)
print(r)