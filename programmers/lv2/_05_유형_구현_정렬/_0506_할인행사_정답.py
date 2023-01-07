# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def getSample(want , number):
    sample = []
    for i in range(len(number)):
        for j in range(number[i]):          
            sample.append(want[i] )
    return sample

def solution(want, number, discount):
    answer = 0
    i = 0
    #sample = getSample(want , number)
    #print(sample)
    while True:
        if i + 10 > len(discount):
            break
        sample = getSample(want , number)
        disSample = discount[i : i + 10]
        j = 0
        check = False
        while j < 10:
            #print(sample , disSample)
            if len(sample) <= 0 or len(disSample) <= 0:
                break
            if sample[0] in disSample:
                index = disSample.index(sample[0])
                del(disSample[index])
                del(sample[0])
            else:
                check = True
                break
            j += 1
        i += 1
        if check == False:
            answer += 1
            
    
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork",
            "rice", "pot", "banana", "apple", "banana"]

r = solution(want , number , discount)
print(r)