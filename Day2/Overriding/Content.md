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

# 동작 재정의하기

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

# 동작 재정의하기 (Overriding)

---

# 클래스가 정의하는 특수한 동작들

<br/>

파이썬에서, 클래스는 `매직메소드`를 사용해 몇가지 특수한 동작들을 정의해요

- 형변환 재정의하기
- 연산자
- for이나 map 등에서 사용 가능한 반복 가능한 객체 (Iterator)
- 함수와 같은 호출 가능한 객체 (Callable)
- ...

<br/>

---

# 메소드 오버라이딩 (Overriding)

<br/>

객체지향 프로그래밍 언어에서, `오버라이딩 (Overriding)` 이란 상속 관계에 있는 클래스에서, 부모 객체의 동작 (메소드)를 자식 객체에서 새로 구현하는 것을 말해요. `다형성`의 일부에요.

---

# 1. 형변환 재정의하기

---

# 문자열 변환 재정의하기, `__str__`

<br/>

```python
class Book:
    def __init__(self, name: str, category: str):
        self.name: str = name
        self.category: str = category

    def __str__(self) -> str:
        return "{제목:" + self.name + ",분류:" + self.category + "}"

print(Book("파이썬 프로그래밍", "전공서"))
# {제목:파이썬 프로그래밍,분류:전공서}
```

---

# 정수형 변환 재정의하기, `__int__`

<br/>

```python
class Hundred:
    """
    세 자리 숫자.
    "abc" = 100*a + 10*b + c
    """
    def __init__(self, a: int, b: int, c: int):
        self.a: int = a
        self.b: int = b
        self.c: int = c

    def __int__(self) -> int:
        return 100 * self.a + 10 * self.b + self.c

print(int(Hundred(1, 2, 3)))
# 123
```

---

# 진리형 변환 재정의하기, `__bool__` 1

<br/>

```python
class Box:
    """
    상자.
    비어있으면 거짓, 내용물이 있으면 참.
    """
    def __init__(self):
        self.content = None
    
    def wrap(self, content):
        self.content = content
    
    def unwrap(self):
        c = self.content
        self.content = None
        return c

    def __bool__(self) -> int:
        return self.content != None
```

---

# 진리형 변환 재정의하기, `__bool__` 2

<br/>

```python
b = Box()
if not b:
    print("현재 상자가 비어있어요.")

b.wrap(42)
if b:
    print("현재 상자에는", b.content,"가 들어있어요.")

b.unwrap()
if not b:
    print("현재 상자가 비어있어요.")
```

---

# 실습 1 : 실수형 변환 재정의하기

<br/>

임의의 숫자 (정수 또는 실수) 값을 저장하는 Box라는 객체가 있다. float형으로 변환하면, 상자 내부의 값을 실수형으로 반환하도록 실수형 변환을 재정의하라.

> 💡 구글링 등을 통해 직접 찾아서 풀어보세요!
> 추천 검색어 : python how to override conversion to float

---

# 실습 1 : 실수형 변환 재정의하기 (정답)

<br/>

```python

class NumberBox:
    """
    숫자를 담는 상자.
    """
    def __init__(self, content):
        self.content = content

    def __float__(self) -> float:
        return float(self.content)
```

---

# 2. 연산자 재정의하기

---

# isinstance()

<br/>

인스턴스가 특정 클래스의 객체가 맞으면 True, 아니면 False를 반환한다.

```python
a = 1
b = "hello"
c = 3.14

if isinstance(a, int):  # a는 정수이므로, 참
    print("a는 정수")
if isinstance(b, int):  # b는 문자열이므로, 거짓
    print("b도 정수")

# 두번째 인자에 튜플로 둘 이상의 클래스를 묶어서 전달하면,
# 튜플 내의 클래스들 중 한 가지의 인스턴스에 해당할 경우 참이에요.

if isinstance(c, (int, float)):  # c는 실수이므로, 참이에요.
    print("c는 정수이거나 실수이다.")
```

---

# 덧셈 재정의하기, `__add__` 1

```python
class IntBox:
    def __init__(self, value: int):
        self.value: int = value
    
    def __str__(self) -> str:
        return "IntBox(" + str(self.value) + ")"
    
    def __add__(self, other):
        if isinstance(other, IntBox):
            # 우항도 NumberBox의 인스턴스일 때
            return IntBox(self.value + other.value)
        elif isinstance(other, int):
            # 우항이 int형 값일 때
            return IntBox(self.value + other)
        # 정의되지 않은 연산은 반드시 NotImplemented 을 반환해야 해요.
        return NotImplemented
```

---

# 덧셈 재정의하기, `__add__` 2

```python
a = IntBox(1)
b = IntBox(2)
c = 3
d = "4"

print(a + b)    # IntBox(3)
print(a + c)    # IntBox(4)
# TypeError: unsupported operand type(s) for +: 'IntBox' and 'str'
print(a + d)
```

---

# 뺄셈 재정의하기, `__sub__` 1

```python
class IntBox:
    def __init__(self, value: int):
        self.value: int = value
    
    def __str__(self) -> str:
        return "IntBox(" + str(self.value) + ")"
    
    def __sub__(self, other):
        if isinstance(other, IntBox):
            # 우항도 NumberBox의 인스턴스일 때
            return IntBox(self.value - other.value)
        elif isinstance(other, int):
            # 우항이 int형 값일 때
            return IntBox(self.value - other)
        # 정의되지 않은 연산은 반드시 NotImplemented 을 반환해야 해요.
        return NotImplemented
```

---

# 뺄셈 재정의하기, `__sub__` 2

```python
a = IntBox(6)
b = IntBox(5)
c = 4
d = "3"

print(a - b)    # IntBox(1)
print(a - c)    # IntBox(2)
# TypeError: unsupported operand type(s) for -: 'IntBox' and 'str'
print(a - d)
```

---

# 실습 2 : 곱셈 재정의하기

<br/>

앞서 만든 IntBox 클래스에 한 개의 매직메소드를 더 오버라이딩 해서, 곱셈도 가능하게 구현해보세요.

> 💡 구글링 등을 통해 직접 찾아서 풀어보세요!
> 추천 검색어 : python how to override multiplication

---

# 실습 2 : 곱셈 재정의하기 (정답)

<br/>

```python
class IntBox:
    def __mul__(self, other):
        if isinstance(other, IntBox):
            # 우항도 NumberBox의 인스턴스일 때
            return IntBox(self.value * other.value)
        elif isinstance(other, int):
            # 우항이 int형 값일 때
            return IntBox(self.value * other)
        # 정의되지 않은 연산은 반드시 NotImplemented 을 반환해야 해요.
        return NotImplemented
```

---

# 실습 3 : 나눗셈 재정의하기

<br/>

앞서 만든 IntBox 클래스와 유사하게, FloatBox라는 새 클래스를 만들어요. 이 클래스는 실수형 값을 다룰 수 있어야 해요. 여기에 한 개의 매직메소드를 더 오버라이딩 해서, 나눗셈도 가능하게 구현해보세요.

> 💡 구글링 등을 통해 직접 찾아서 풀어보세요!
> 추천 검색어 : python how to override division

---

# 실습 3 : 나눗셈 재정의하기 (정답)

<br/>

```python
class FloatBox:
    def __init__(self, value: float):
        self.value: float = value
    
    def __str__(self) -> str:
        return "FloatBox(" + str(self.value) + ")"
    
    def __div__(self, other):
        if isinstance(other, FloatBox):
            # 우항도 FloatBox 인스턴스일 때
            return FloatBox(self.value / other.value)
        elif isinstance(other, (int, float)):
            # 우항이 int형 또는 float형 값일 때
            return FloatBox(self.value / other)
        # 정의되지 않은 연산은 반드시 NotImplemented 을 반환해야 해요.
        return NotImplemented
    ...
    # __add__, __sub__, __mul__도 IntBox를 FloatBox로 바꾸고,
    # isinstance 부분을 바꿔주면 돼요.
```

---

# 3. 반복 가능한 객체 만들기

---

# 반복 가능한 객체

<br/>

이전에, for문에서 `range`나 리스트를 사용해 반복을 도는 코드를 보여줬어요.

```python
for i in range(10):  # 0 ~ 9
    print(i)

for i in [1, 3, 5, 7, 9]:
        print(i)  # 1 3 5 7 9
```

여기서, `range`와 리스트는 모두 반복 가능한 객체들이에요.

---

# 반복 가능한 객체 만들기 1

<br/>

파이썬에서, 반복 가능한 객체는 `__iter__`과 `__next__`의 2가지 매직메소드를 재정의해서 구현해요.
간단하게, range를 따라 만들어볼게요.

---

# 반복 가능한 객체 만들기 2

<br/>

`range` 객체는 start, end, step 순으로 최대 3가지 인자를 받아요.start 인자부터 시작해서, end보다 작을 동안 step씩 증가하면서 반복해요.

<br/>

```python
class MyRange:
    def __init__(self, start: int, end: int, step: int):
        self.end: int = end
        self.step: int = step
        self.index: int = start
```

---

# 반복 가능한 객체 만들기 3

<br/>

반복 가능한 (Iterable한) 객체는 `__iter__` 매직메소드를 정의해요.
이 매직메소드는 내부적으로 호출되어, 반복자 (Iterator)를 얻어요.
우리가 만들 MyRange는 별도의 Iterator 없이 그 자체가 반복자로도 기능하게끔 구현하려고 해요.
그러므로, `__iter__`은 self를 그대로 반환해주면 돼요.

<br/>

```python
class MyRange:
    ...
    def __iter__(self):
        return self
```
---

# 반복 가능한 객체 만들기 4

<br/>

반복자(Iterator)는 `__next__` 매직메소드를 정의해요.
이 매직메소드는 내부적으로 호출되어, for문 등에서 반복할 때, 매 반복마다 한번씩 호출되어 값을 전달해요.
만약 반복이 끝났다면, `StopIteration` 예외를 발생시켜요.

<br/>

```python
class MyRange:
    ...
    def __next__(self):
        if self.index == self.end:
            # 반복이 끝났으므로 StopIteration` 예외를 발생시켜요.
            raise StopIteration()
        v = self.index
        self.index += 1
        return v
```
---

# 반복 가능한 객체 만들기 5

<br/>

이제 앞서 만든 MyRange와 range의 출력 결과를 비교해볼게요.

<br/>

```python
for i in range(5):
    print(i)
for i in MyRange(0, 5, 1):
    print(i)
```

---

# 실습 4 : 피보나치수열 반복자

<br/>

N을 인자로 받아, 피보나치수열의 N번째 항까지 반복하는 반복자(Iterator)를 만들어보세요.

<br/>

> 💡 피보나치 수열
> 피보나치 수열은 재귀적으로 정의되는 수열이에요.
> 
> $f_1 = 1$
> $f_2 = 2$
> $f_n = f_{n-2} + f_{n-1}$

---

# 실습 4 : 피보나치수열 반복자 (힌트)

<br/>

```python
class Fibonacci:
    def __init__(self, n: int):
        self.n: int = n
        self.index: int = 1     # 현재 계산하는 항이 몇번째 항인지 저장하기
        self.prev_1: int = 1      # n-1 항을 저장하기
        self.prev_2: int = 1      # n-2 항을 저장하기
    
    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        if self.index > self.n:
            # N번째 항까지 출력하면, 반복자를 종료.
            raise StopIteration()
        
        v: int = 0          # 현재 반복에서 반환할 값
        if self.index < 3:
            v = 1

        # ( 여기에 코드 작성 )
        self.index += 1
        return v
```
---
# 실습 4 : 피보나치수열 반복자 (정답) 1

<br/>

```python
class Fibonacci:
    def __init__(self, n: int):
        self.n: int = n
        self.index: int = 1     # 현재 계산하는 항이 몇번째 항인지 저장하기
        self.prev_1: int = 1      # n-1 항을 저장하기
        self.prev_2: int = 1      # n-2 항을 저장하기
    
    def __iter__(self):
        return self
```

---
# 실습 4 : 피보나치수열 반복자 (정답) 2 

```python
    def __next__(self) -> int:
        if self.index > self.n:
            # N번째 항까지 출력하면, 반복자를 종료.
            raise StopIteration()
        
        v: int = 0  # 반환할 값
        if self.index < 3:
            v = 1
        else:
            v = self.prev_1 + self.prev_2
            self.prev_1 = self.prev_2
            self.prev_2 = v

        self.index += 1
        return v

for i in Fibonacci(5):
    print(i)
        
```

---

# 4. 호출 가능한 객체 만들기

---

# 호출 가능한 객체

<br/>

호출 가능한 (Callable한) 객체는 함수처럼 호출 가능한 객체에요.

---

# 호출 가능한 객체의 구현

<br/>

호출 가능한 (Callable한) 객체는 `__call__` 매직메소드를 정의해요.

```python
class Add:
    def __call__(self, x, y):
        return x + y

add = Add()
print(add(1, 2))    # 3
```

---

# 실습 5 : N을 곱하는 객체 만들기

<br/>

생성자 (`__init__`)의 인자로 N을 받고, 이후 호출시 x를 받아 N * x를 계산해주는 객체를 만드세요.

```python
# 예시
class MultiplyN:
    pass

mul3 = MultiplyN(3)
print(mul3(4))      # 12
mul5 = MultiplyN(5)
print(mul5(4))      # 20
```

---

# 실습 5 : N을 곱하는 객체 만들기 (정답)

<br/>

```python
# 예시
class MultiplyN:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, x):
        return self.n * x

mul3 = MultiplyN(3)
print(mul3(4))      # 12
mul5 = MultiplyN(5)
print(mul5(4))      # 20
```

---

# 요약

1. 파이썬에서는 `매직메소드` 라 불리는 특수한 메소드들을 재정의해, 객체의 특수한 동작들을 재정의할 수 있다.

2. 정의 가능한 동작들은 아래와 같다.
    - 형변환
    - 연산자
    - 반복 가능한 객체 (Iterator)
    - 호출 가능한 객체 (Callable)
    - ...

---

# 강의를 들어줘서 고마워요 :wink:
