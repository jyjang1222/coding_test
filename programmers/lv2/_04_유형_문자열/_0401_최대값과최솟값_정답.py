# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    arr = s.split(" ")
    print(arr)
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    answer += str(min(arr))
    answer += ' '
    answer += str(max(arr))
    return answer

s = "1 2 3 4"
r = solution(s)
print(r)

# 음수도 인식해야하므로 형변환을 해서 저장하면된다. 