# 프로그래머스 문제풀이

## 배울사항

### 포문을 이용해서 0으로 가득찬 리스트 만들기

```python
test = [0 for i in range(5)]
print(test) # [0, 0, 0, 0, 0]
```

### find() 메서드

```python
"""
[1]  find 함수는 문자열데이터에 특정값이 있는지 확인해준다.
    특정값을 찾으면 인덱스를 반환해준다.
    못찾으면 -1을 반환해준다.
"""

a = "abcdefg"
test1 = a.find("b") # 1
print(test1)

test2 = a.find("z") # -1
print(test2)
```

### replace() 메서드

```python
str = 'hello world'
str = str.replace('o', '', 1)
print(str) # hell world
```
- 값이 문자열일때 쓸수있는 메서드이다.
- 변경할 문자를 지정하고 다른 문자로 치환할수있다.
- replace(str, str, cnt)
- 인자는 차례로 변경될 문자, 치환할 문자, 수행횟수

### in, not in 키워드

```python
str = 'hello world'
bool = False
if 'hell' in str:
    bool = True
print(bool) # True
```
- 데이터 안에 값이 있는지없는지 반환하는 키워드이다.
- in 키워드는 안에 있으면 true반환 없으면 false반환 이고 not in은 그 반대이다.

### insert()

```python
arr = [10,20,30]
arr.insert(2, 500)
# [10,20,500,30]
```

### index()

```python
arr = [10,20,30]
print(arr.index(20)) # 1
```

### count()
```python
arr = [1] * 10
print(arr.count(1)) # 10
```

- 해당 값의 갯수를 반환한다.

### reverse()
```python
arr = [1,2,3,4,5]
arr.reverse()
print(arr) # [5,4,3,2,1]
```

### sort()
```python
arr = [1,2,3,4,5]
arr.reverse()
print(arr) # [5,4,3,2,1]
arr.sort()
print(arr) # [1,2,3,4,5]
# 내림차순
arr.sort(reverse=True) # [5,4,3,2,1]
# 오름차순
arr.sort(reverse=False) # [1,2,3,4,5]
```

### clear()
```python
arr = [1,2,3,4,5]
arr.clear()
print(arr) # []
```

### remove() , del

```python
arr = [1,2,3,4,5]
del arr[2] # [1,2,4,5]
del arr[1:3] # [1,5]
arr.remove(5) # [1]
arr.remove(a[0]) # []
```

### 리스트 연결

```python
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c) # [1,2,3,4,5,6]
d = a * 3
print(d) # [1,2,3,1,2,3,1,2,3]
```

### 리스트 복사

```python
a = [10,10,10,10,10]
b = a.copy()
```

### 배열을 만드는 여러가지 방법

```python
max_product_number = 10
counter = [0 for _ in range(max_product_number + 1)]
print(counter)

arr = [1] * len(counter)
print(arr)

arr2 = list(range(0,10))
print(arr2)
```