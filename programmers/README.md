# 프로그래머스 문제풀이
## 배울사항
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