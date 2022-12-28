# 백준 문제풀이

## 문제풀이시 입력 방식

### input()
- 한 줄의 문자열을 입력

### split()
- a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다. 만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다. 
 
### input().split()

- 여러개 입력받을 때. 리스트 형태로 반환
 
### map
- map(데이터 타입, 리스트) : 리스트 원소들을 해당 데이터 타입으로 변환

```python
# input() 이용
a, b = map(int, input().split())
print(a+b)

# sys.stdin.readline() 이용
import sys
a, b = map(int, sys.stdin.readline().split())
print(a+b)
```

일단 후자가 더 빠른 방식이다.