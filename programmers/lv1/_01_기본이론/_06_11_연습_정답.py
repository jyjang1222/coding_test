"""
    [문제]
        b의 값이 a에 있으면 a의 값에서 b의 값을 전부 삭제하시오.
    [정답]
        a = [1,7]
"""

a = [1,5,7,8]
b = [4,5,8]


for j in range(len(b)):
    if b[j] in a:
        idx = a.index(b[j])
        del(a[idx])
print(a)


