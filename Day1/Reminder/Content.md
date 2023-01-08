---
marp: true
theme: default
class:
    - invert
paginate: true
math: mathjax
---

<style>
  :root {
    --color-fg-default: #c9d1d9;
    --color-canvas-default: #0d1117;
  }
</style>

# 여름방학 특강 복습

<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<h3 style="text-align: right">숭실대학교 소프트웨어학부 김민준</h3>

---

# 강사 소개

```json
{
    "이름": "김민준",
    "학력": {
        "영훈고등학교": {
            "입학": 2019,
            "졸업": 2022,
            "동아리": {
                "디지털공작반": {"from": 2020, "to": 2022, "spec": "1기부장"},
                "MAKERS": {"from": 2019, "to": 2019}
            }
        },
        "숭실대학교": {
            "전공": "소프트웨어학부",
            "입학": 2022
        }
    }
}
```

---

# 강사 소개

```json
{
    "Github": "Lapis0875",
    "경력": {
        "Python": {
            "year": 4,
            "projects": [
                {"name": "bluearchive"},
                {"name": "D2Wiki"},
                {"name": "proxy-www.py"},
                // ...
            ]
        },
        "Kotlin": {...},
        "Java": {...},
        "C/C++": {...}
    }
}
```

---

# 1. 변수와 자료형

---

# 변수

<br/>
프로그래밍에서 메모리 상에 데이터를 저장하는 방법.

<br/>
<br/>

```python
a = 42
b = "hello"
c = 3.5
d = True
```

---

# 변수 이름 규칙

<br/>

- 숫자를 포함할 수 있다. (0~9)
- 숫자로 시작할 수는 없다.
- 밑줄( _ )을 포함할 수 있다.
- 예약어(키워드)는 포함할 수 없다.
  - 예약어 : if, for 등 언어 자체적으로 사용되는 단어들.

---

# 변수 이름 규칙

<br/>

- 대소문자를 구분한다. 대소문자만 사용할 수 있다.
  - 파이썬의 경우 유니코드를 지원해, 변수 이름으로 영어 이외의 글자들을 사용 할 수 있다.
  - 하지만, 다른 사람들도 읽을 수 있는 코드를 지향해야 하므로 변수 등의 이름은 영어로 적는 것이 관례.
    - 해외 사이트에 질문하거나 코드를 공유하는 등의 경우가 많음.

---

# 2. 원시 자료형

---

# 정수형

<br/>

- int : integer의 줄임말.
- 정수 값들을 표현.

<br/>
<br/>

```python
i: int = 42
j: int = -1
```

---

# 실수형

<br/>

- float : floating point numbers (부동소수점) 의 줄임말.
  - 부동소수점에 대해서는 구글링!
- 소수점을 포함하는 실수 값들을 표현.

<br/>
<br/>

```python
f: float = 3.14
g: float = 1.7
```

---

# 진리형

<br/>

- 참 / 거짓을 나타냄.
- `True` 또는 `False`의 값을 가짐.

<br/>
<br/>

```python
t: bool = True
f: bool = False
```

---

# 문자열

<br/>

- str : string의 줄임말.
- 작은 따옴표 (`’`) 또는 큰 따옴표 (`”`) 로 감싼 글자들을 값으로 함.

<br/>
<br/>

```python
text: str = "Hello World!"
```

---

# 3. 컨테이너 자료형

---

# 리스트 (list)

<br/>

기본 자료형이 단순한 값을 의미한다면, 컨테이너 자료형은 다른 자료형을 보관하는 자료형이다.

- 가변 길이의 배열.
- 새 원소를 추가하거나 기존 원소를 삭제할 수 있다.
- 정수 값인 `인덱스`로 내부 원소에 접근할 수 있다.

<br/>

```python
l: list = [1, 2, 3, 4, 5]
```

---

# 튜플 (tuple)

<br/>

기본 자료형이 단순한 값을 의미한다면, 컨테이너 자료형은 다른 자료형을 보관하는 자료형이다.

- 불변 길이의 배열.
- 리스트와 유사하지만, 튜플을 만들 때 가지고 있던 원소들을 변경할 수 없다.
- 정수 값인 `인덱스`로 내부 원소에 접근할 수 있다.

<br/>


```python
t: tuple = (1, 2, 3, 4, 5)
```

---

# 딕셔너리 (dict)

<br/>

기본 자료형이 단순한 값을 의미한다면, 컨테이너 자료형은 다른 자료형을 보관하는 자료형이다.

- dict : dictionary의 줄임말.
- 리스트와 튜플과는 달리, `키:값` 의 쌍으로 원소를 저장한다.
- 내부 원소에 접근할 때는 인덱스가 아닌 `키` 를 사용한다.

<br/>

```python
d: dict = {"name": "홍길동", "age": 21}
```

---

# 4. 연산자

---

# 1) 수 사이의 연산

- int와 float 사이의 연산의 경우, 표현 범위가 더 큰 float로 변환됩니다.

<br/>

## 덧셈

```python
a: int = 5 + 4 = 9
b: float = 5.0 + 4 = 9.0
c: float = 5 + 4.0 = 9.0
d: float = 5.0 + 4.0 = 9.0
```

---

# 1) 수 사이의 연산

- int와 float 사이의 연산의 경우, 표현 범위가 더 큰 float로 변환됩니다.

<br/>

## 뺄셈

```python
a: int = 5 - 4 = 1
b: float = 5.0 - 4 = 1.0
c: float = 5 - 4.0 = 1.0
d: float = 5.0 - 4.0 = 1.0
```

---

# 1) 수 사이의 연산

- int와 float 사이의 연산의 경우, 표현 범위가 더 큰 float로 변환됩니다.

<br/>

## 곱셈

```python
a: int = 5 * 4 = 20
b: float = 5.0 * 4 = 20.0
c: float = 5 * 4.0 = 20.0
d: float = 5.0 * 4.0 = 20.0
```

---

# 1) 수 사이의 연산

<br/>

- int와 int끼리 나눠도 무조건 float가 나옵니다!

## 나눗셈

```python
a: float = 5 / 4 = 1.25
b: float = 5.0 / 4 = 1.25
c: float = 5 / 4.0 = 1.25
d: float = 5.0 / 4.0 = 1.25
```

---

# 1) 수 사이의 연산

<br/>

- int와 float 사이의 연산의 경우, 표현 범위가 더 큰 float로 변환됩니다.

## 제곱

```python
a: int = 5 ** 2 = 25
b: float = 5.0 ** 2 = 25.0
c: float = 5 ** 2.0 = 25.0
d: float = 5.0 ** 2.0 = 25.0
```

---

# 1) 수 사이의 연산

<br/>

- int와 float 사이의 연산의 경우, 표현 범위가 더 큰 float로 변환됩니다.

## 나머지 ($mod$)

```python
a: int = 5 % 2 = 1
b: float = 5.0 % 2 = 1.0
c: float = 5 % 2.0 = 1.0
d: float = 5.0 % 2.0 = 1.0
```

---

# 1) 수 사이의 연산

<br/>

- int와 float 사이의 연산의 경우, 표현 범위가 더 큰 float로 변환됩니다.

## 몫

```python
a: int = 5 // 2 = 2
b: float = 5.0 // 2 = 2.0
c: float = 5 // 2.0 = 2.0
d: float = 5.0 // 2.0 = 2.0
```

---

# 2) 문자열 연산

<br/>

## 문자열 합치기

```python
a = "Hello"
b = "World"
print(a + b)  # HelloWorld
```
    
## 문자열 반복하기

```python
text = "Hello"
print(text * 3)  # HelloHelloHello
```

---

# 5. 제어문

---

# 비교 연산자

비교연산자를 사용해 두 값을 비교한 결과는 진리형(bool) 타입의 값인 True 또는 False로 표현된다.

- 두 값이 같다 : `==`
- 두 값이 다르다 : `!=`
- 좌항이 우항보다 크다 : `>`
- 좌항이 우항보다 작다 : `<`
- 좌항이 우항보다 크거나 같다 : `>=`
- 좌항이 우항보다 작거나 같다 : `<=`

---

# 조건문 - if

if문의 조건이 참일 때, if 블럭 (들여쓰기 된 부분) 내의 코드를 실행한다.

```python
# 문법
if {condition}:
        {body}
```

```python
# 예문
num = int(input("양의 정수 입력 : "))
if num >= 10:
        print("두 자리 이상의 수를 입력했습니다.")
```

---

# 조건문 - else

if문의 조건이 거짓일 때, else 블럭 (들여쓰기 된 부분) 내의 코드를 실행한다.

```python
# 문법
if {condition}:
        {body1}
else:
        {body2}
```

```python
# 예문
num = int(input("양의 정수 입력 : "))
if num >= 10:
        print("두 자리 이상의 수를 입력했습니다.")
else:
        print("한 자리 수 입니다.")
```

---

# 조건문 - elif

if문의 조건이 거짓일 때, 이후에 elif문이 있다면 elif문의 조건을 판단한다. elif문은 여러개 연속해 사용할 수 있다.

```python
# 문법
if {condition1}:
        {body1}
elif {condition2}:
        {body2}
    ...
else:
        {bodyN}
```

---

# 조건문 - elif

if문의 조건이 거짓일 때, 이후에 elif문이 있다면 elif문의 조건을 판단한다. elif문은 여러개 연속해 사용할 수 있다.

```python
# 예문
num = int(input("양의 정수 입력 : "))
if num >= 100:
        print("세 자리 이상의 수를 입력했습니다.")
elif num >= 10:
        print("두 자리 수 입니다.")
else:
        print("한 자리 수 입니다.")
```

---

# 반복문 - for

반복 가능한 객체 (Iterator)의 각각의 원소를 가져와 반복. 전체 원소에 대해서 진행.

- `반복 가능한 객체`에 대해서는 나중에 설명할게요!

```python
for i in range(10):  # 0 ~ 9
    print(i)

for i in [1, 3, 5, 7, 9]:
        print(i)  # 1 3 5 7 9
```

---

# 반복문 - while

조건이 참일 동안 계속 반복.

```python
i = 0
while i < 10:
    print(i)  # 0 ~ 9 출력
    i += 1

while True:  # 무한루프
    print("Loop!")
```

---

# 6. 함수

---

# 함수

수학에서의 함수와 같이, 인자를 받고 결과를 반환할 수 있다.

```python
def function(argument):
    # do something
    return result
```

---

# 인자와 반환값 모두 가지는 함수

<br/>

```python
def square(a: int) -> int:
    return a * a

def add(a: int, b: int) -> int:
    return a + b
```

---

# 인자는 받지만 값을 반환하지 않는 함수

<br/>

```python
def whatis(data):
    print("data is", data)

def whisper(text: str):
    print(text.lower())
```

---

# 인자는 받지 않지만 값을 반환하는 함수

<br/>

```python
def universe_answer() -> int:
    return 42

def get_name() -> str:
    return "홍길동"
```

---

# 인자도 받지 않고 값도 반환하지 않는 함수

<br/>

```python
def greeting():
    print("Hello!")

def farewell():
    print("Good bye!")
```

---

# 함수의 인자

## 위치 인자 & 키워드 인자

```python
def say(phrase, target):
    print("나는", target, "에게 다음과 같이 말했다 :")
    print(phrase)
```

<br/>

이 함수를 호출할 때, 인자를 전달할 수 있는 방법은 두 가지가 있다.

```python
say("안녕!", "홍길동")
say(phrase="안녕!", target="홍길동")
```

---

# 위치 인자

<br/>

```python
say("안녕!", "홍길동")
```

<br/>

- 함수 인자에 값을 바로 전달하는 통상적인 방식이다.
- `위치 인자`라고 부른다.
- 함수에서는 인자가 정의된 순서대로 값을 할당받는다.

---

# 키워드 인자

<br/>

```python
say(phrase="안녕!", target="홍길동")
```

<br/>

- 각 값을 어느 인자에 전달할지 인자의 이름을 명시해 전달하는 방식이다.
- `키워드 인자`라고 부른다.
- 함수에 정의된 인자의 순서와 무관하게 임의의 순서대로 인자에 값을 할당할 수 있다.

---

# 7. 함수형 프로그래밍

---

# 일급 객체

<br/>

함수의 인자, 또는 변수에 할당할 수 있는 객체를 일급 객체라고 부른다. 대표적으로, 기본 자료형의 값들이나, 다른 객체의 참조 정도 등이 있다.

```python
def function(arg):
    print(arg)

a: int = 5          # 일급 객체
b: str = "Hello"    # 일급 객체
function(a)
function(b)
```

---

# 함수형 프로그래밍에서의 일급 객체

<br/>

함수평 프로그래밍에서는 “함수” 또한 일급 객체로 취급해, 함수를 다른 함수에 전달하거나 변수에 저장할 수 있다.

<br/>

```python
def say(text, method):
    print(method(text))

def whisper(text):
    return text.lower() + "..."

def yell(text):
    return text.upper() + "!"

say("Hello", whisper)   # hello...
say("Hello", yell)      # HELLO!
```

---

# map

map은 list, tuple 등의 순환 가능한(Iterable한) 객체의 각 원소에 인자로 받은 함수를 적용해, 새 순환 가능한 객체 (Iterator)을 만든다.

> 💡 순환 가능하다 (Iterable) / 순환 가능한 객체 (Iterator)
> list, tuple, range 처럼 for문 등에서 사용할 수 있는 객체를 말해요.

<br/>

```python
l = [1, 2, 3, 4, 5]
print(l)    # 1, 2, 3, 4, 5

def square(x):
    return x ** 2

l2 = list(map(square, l))
print(l2)  # 1, 4, 9, 16, 25
```

---

# filter

filter는 순환 가능한 객체의 각 원소에 인자로 받은 함수를 적용해, 함수의 반환값이 참(`True`)인 원소들만 추려낸 새 순환 가능한 객체를 만든다.

<br/>

```python
l = [1, 2, 3, 4, 5]
print(l)  # 1, 2, 3, 4, 5

def isodd(x):
    return x % 2 == 1

l2 = list(filter(isodd, l))
print(l2)  # 1, 3, 5
```

---

# reduce

reduce는 순환 가능한 객체의 각 원소들을 함수를 사용해 누적한다.

<br/>

```python
from functools import reduce  # reduce는 functools 모듈에 포함된 함수로, import해야 쓸 수 있다.

l = [1, 2, 3, 4, 5]
print(l)  # 1, 2, 3, 4, 5

def sum(prev, cur):
    return prev + cur

def mul(prev, cur):
    return prev * cur

print("1~5까지 합 :", reduce(sum, l))
print("1~5까지 곱 :", reduce(mul, 1))
```

---

# reduce


<br/>
세 번째 인자를 통해 초기값을 설정할 수 있다.

```python
from functools import reduce
# reduce는 functools 모듈에 포함된 함수로, import해야 쓸 수 있다.

def add(prev, cur):
    print((prev, cur))
    return prev + cur

l = [1, 2, 3]
```

---

# reduce

세 번째 인자를 통해 초기값을 설정할 수 있다.

<br/>

```python
"""
초기값 인자를 주지 않을 경우, 
순환 가능한 객체의 첫 번째 인자가 초기값이 된다.
이후, 두 번째 인자부터 reduce를 통해 반복한다.
"""

print(reduce(add, l))
# (1, 2)
# (3, 3)
# 6
```

---

# reduce

세 번째 인자를 통해 초기값을 설정할 수 있다.

<br/>

```python
"""
초기값 인자를 줄 경우,
순환 가능한 객체의 첫 번째 인자부터 reduce를 통해 반복한다.
"""

print(reduce(add, l, 0))
# (0, 1)  <-- 초기값이 0으로 설정되었다!
# (1, 2)
# (3, 3)
# 6
```

---

# 강의를 들어줘서 고마워요 :wink:
