# https://school.programmers.co.kr/learn/courses/30/lessons/12941
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    B.reverse()
    print(A , " " , B)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer


A = [1,4,2]
B = [5,4,4]
r = solution(A , B)
print(r)