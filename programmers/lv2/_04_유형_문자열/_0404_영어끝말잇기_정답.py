# https://school.programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    temp = [words[0]]
    c = 0
    d = 0
    answer = [c , d]
    for i in range(1, len(words)):
        a = temp[-1]
        b = words[i]
        if a[-1] == b[0]:
            if b in temp:
                c = i % n + 1
                d = i // n + 1
                answer = [c , d]
                break
            temp.append(b)
        else:
            c = i % n + 1
            d = i // n + 1
            answer = [c , d]
            break
    return answer
n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
r = solution(n , words)
print(r)