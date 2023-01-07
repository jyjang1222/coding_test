import math
def solution(begin, end):
    answer = []
    arr = [1 for i in range(end-begin + 1)]
    if begin == 1:
        arr[0] = 0
        i = begin + 1
        index = 1
    else:
        i = begin
        index = 0
    while i <= end:
        #root = int(math.sqrt(i))
        j = 2
        while j * j < i:
            if i % j == 0 and i // j <= 10000000:           
                a = i // j
                arr[index] = a
                break
            j += 1
        index += 1
        i += 1
    print(arr)
    return arr


b , end = 1000000000, 1000000100
r = solution(b , end)
print(r)