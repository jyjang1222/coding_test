'''
머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ babbling의 길이 ≤ 100
1 ≤ babbling[i]의 길이 ≤ 15
babbling의 각 문자열에서 "aya", "ye", "woo", "ma"는 각각 최대 한 번씩만 등장합니다.
즉, 각 문자열의 가능한 모든 부분 문자열 중에서 "aya", "ye", "woo", "ma"가 한 번씩만 등장합니다.
문자열은 알파벳 소문자로만 이루어져 있습니다.

예시
["aya", "yee", "u", "maa", "wyeoo"],	1
["ayaye", "uuuma", "ye", "yemawoo", "ayaa"],	3
'''

# 내풀이
def solution(babbling):
    arr = ['aya', 'ye', 'woo', 'ma']
    arr2 = ['aya', 'ye', 'woo', 'ma']
    cnt = 0
    
    # 조합2
    for i in arr:
        for j in arr:
            if i != j:
                tmp = i + j
                arr2.append(tmp)
                tmp = ''
    # 조합3
    for i in arr:
        for j in arr:
            for k in arr:
                if i != j and i != k and j != k:
                    tmp = i + j + k
                    arr2.append(tmp)
                    tmp = ''
    # 조합4        
    for i in arr:
        for j in arr:
            for k in arr:
                for m in arr:
                    if i != j and i != k and i != m and j != k and j != m and k != m:
                        tmp = i + j + k + m
                        arr2.append(tmp)
                        tmp = ''
                
            
    for i in arr2:
        for j in babbling:
            if i == j:
                cnt += 1
    answer = cnt
    # print(arr2)
    return answer

test = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa", "ayayeaya", "woomayeaya"]
print(solution(test))