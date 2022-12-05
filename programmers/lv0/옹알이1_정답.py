test = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa", "ayayeaya", "woomayeaya"]

# 정답
def solution(babbling):
    word = ['aya', 'ye', 'woo', 'ma']
    count = 0
    for i in babbling:
        for j in word:
            if j in i:
                i = i.replace(j, '*', 1)
        i = i.replace('*', '')
        if i == '':
            count += 1
    answer = count
    return answer

print(solution(test))