max_product_number = 10
counter = [0 for _ in range(max_product_number + 1)]
print(counter)

arr = [1] * 10
print(arr)
print(arr.count(1))

arr2 = list(range(0,10))
print(arr2)

print(arr2[2:4])
print(arr2.index(5))


arr4 = [1,2,3,4,5]
del arr4[2] # [1,2,4,5]
del arr4[1:3] # [1,5]
arr4.remove(5) # [1]
arr4.remove(arr4[0]) # []
print(arr4)