inputNum = input('수를 입력하세요.\n')
num = int(inputNum)

count = 0
for i in range(1, num+1):
    current = i
    while current != 0:
        if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
            print(i, end=" ")
            count += 1
        current //= 10

print(num, count)

arr = [1,2,3,4,5]
print(arr[1:3]) 
print(arr)