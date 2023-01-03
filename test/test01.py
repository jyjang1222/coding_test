# inputNum = input('수를 입력하세요.\n')
# num = int(inputNum)

# count = 0
# for i in range(1, num+1):
#     current = i
#     while current != 0:
#         if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
#             print(i, end=" ")
#             count += 1
#         current //= 10

# print(num, count)

# arr = [1,2,3,4,5]
# print(arr[1:3]) 
# print(arr)

n = 118372

s1 = str(n) # 숫자를 문자로 변환
print(s1) # "118372"

s2 = sorted(s1)	#  sorted를 이용해서 각각을 잘라서 리스트로변환후 오름차순정렬 
print(s2) # ['1', '1', '2', '3', '7', '8']

s3 = sorted(map(int, s2), reverse=True)

print(s3) # [8, 7, 3, 2, 1, 1]