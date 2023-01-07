# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ""
    while True:
        if len(s) <= 0:
            break

        # 맨앞이 공백인경우 제거한다. 제거하기전에 answer 에 공백저장
        if s[0] == " ":   
            answer += " "
            s = s[1:]
            continue     
        
        if " " in s:        # 맨뒤가 아닐때
            a = s.index(" ")
            temp = s[:a]  
            head = temp[0]
            tail = temp[1:]            
            s = s[a:]
        else:               # 맨뒤일때  
            head = s[0]
            tail = s[1:]  
            s = ""

        head = head.upper()
        tail = tail.lower()         
        answer = answer + head + tail

    return answer
s = "     3people     unFollowed     me"	

r = solution(s)
print(r)
