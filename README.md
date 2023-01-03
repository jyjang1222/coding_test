# 코딩테스트 모음

## 배열 및 문자열 배울사항

### 특정 수로 가득찬 리스트 만들기

```python
test = [0 for i in range(5)]
print(test) # [0, 0, 0, 0, 0]

arr = [1] * 5
print(arr) # [1, 1, 1, 1, 1]
```

### 배열 자르기

```python
arr = [1,2,3,4,5]
print(arr[1:3]) # [2, 3]

text = "java python javascript"

a = text[0:4] # java   
b = text[:4] # java
c = text[7:14] # thon ja
d =  text[7:] # thon javascript
e = text[5:11] # python
f = text[12:22] # javascript
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

arr = [1, 2, 3]

if 2 in arr:
    bool = False
print(bool) # False
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

### split()

```python
string = 'abc,def,ghi'
arr = string.split(',') # [abc, def, ghi]
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

### keys()

```python
"""
[1] 딕셔너리 키묶음찾기
    딕셔너리는 keys() 함수를 이용해서 key값들을 모두 찾은후, key로 value를 찾을수있다. 
"""
di = {"a" : 0 , "b" : 1 , "c" : 2}
print(di.keys()) # ['a', 'b', 'c']
"""
[1] 딕셔너리 출력
    for 문을 활용해서 아래와 같이 출력할수있다.
"""
for key in di.keys():
    print(key , " " , di[key])
```

### upper(), lower()

```python
"""
    [대문자]
        upper() 함수는 문자열의 모든알파벳을 대문자로 바꿔준다. 알파벳이 아닌 문자는 아무영향없다.
"""
a = "asd12vsdads"
b = a.upper()
print(b) # ASD12VSDADS

"""
    [소문자]
        lower() 함수는 문자열의 모든알파벳을 소문자로 바꿔준다. 알파벳이 아닌 문자는 아무영향없다.
"""
c = "ASDAasdSDA124SADS"
d = c.lower()
print(d) # asdaasdsda124sads
```

### list(), map()

```python
"""
    list() 함수는 문자열을 리스트로 만들어준다. 
"""
"""
    map() 함수는 문자로구성되어있는리스트를 정수로 변환해준다. 아래함수와 같이써야한다.
    list(arr)
"""

"""
[문제]
    12345 를 뒤집어서 리스트로 변환하시오. 
[정답]
    [5,4,3,2,1]
"""

n = 12345
s1 = str(n) # 12345 => "12345"
arr = list(s1) # 문자열을 리스트로 변환 
print(arr) # ['1', '2', '3', '4', '5']

arr.reverse() # 뒤집기

arr = map(int , arr) # 리스트의 값들을 전부 정수로 변환
arr = list(arr) # 변환된 map을 다시 list로 변환 
print(arr)
```

### sorted()

```python
n = 118372

s1 = str(n) # 숫자를 문자로 변환
print(s1) # "118372"

s2 = sorted(s1)	#  sorted를 이용해서 각각을 잘라서 리스트로변환후 오름차순정렬 
print(s2) # ['1', '1', '2', '3', '7', '8'] 

s3 = sorted(map(int, s2), reverse=True)
 # map함수를 이용하여 리스트의 값들을 전부 정수로 변환

print(s3) # [8, 7, 3, 2, 1, 1]
```

