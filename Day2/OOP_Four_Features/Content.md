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

# 객체지향의 4대 개념

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

# 객체지향 프로그래밍의 4가지 특징

---

# 4가지 특징들

<br/>

객체지향 프로그래밍은 아래 **4가지 주요한 특징들**을 가져요.

- 추상화 (Abstraction)
- 캡슐화 (Encapsulation)
- 상속 (Inheritance)
- 다형성 (Polymorphism)

<br/>

---

# 1. 추상화 (Abstraction)

---

# 추상화 (Abstraction)

<br/>

> 💡 **"객체들 간에 공통되는 속성이나 동작을 하나로 추출해내는 작업"**

<br/>

추상적인 개념에 의존하여 설계해야 코드를 더 유연하게 작성할 수 있어요.

---

# 추상화 예제 - 도서 1

<br/>

```python
"""
신데렐라, 헨젤과 그레텔 등은 모두 "제목" 이라는 속성과,
"책을 대여하는" 행위를 가져요.
이들은 공통된 동작이므로 추상화할 수 있어요.
"""
class Book:
    def __init__(self, name: str):
        self.name: str = name
    
    def info(self):
        print(self.name)
    
    def borrow(self, who: str):
        print(who, "가", self.name, "을(를) 빌렸습니다.")
```

---

# 추상화 예제 - 도서 2

<br/>

```python
book1 = Book("신데렐라")
book2 = Book("헨젤과 그레텔")

book1.info()
book2.info()

book1.borrow("철수")    # 철수 가 신데렐라 을(를) 빌렸습니다.
book2.borrow("영희")    # 영희 가 헨젤과 그레텔 을(를) 빌렸습니다.
```

---

# 2. 캡슐화 (Encapsulation)

---

# 캡슐화 (Encapsulation) 1

<br/>

> 💡 **"정보 은닉화를 통해 높은 응집도, 낮은 결합도를 유지할 수 있도록 설계하는 것"**

한 곳에서 변화가 일어나도 다른 곳에 미치는 side effect를 최소화 시키는 것.

즉, 객체 내부의 어떤 동작에 대한 구현을 숨겨서, 외부에서의 접근으로 인해 객체가 손상되는 일을 방지할 수 있다.

<br/>

---

# 캡슐화 (Encapsulation) 2

> 객체 각각은 독립적으로 작용할 수 있도록 응집도가 높아야 하고, 다른 모듈을 참조하는 결합도는 낮아야 함!

---

# 3. 상속 (Inheritance)

---

# 상속 (Inheritance)

<br/>

> **"여러 개체들이 지닌 공통된 특성을 부각시켜 하나의 개념이나 법칙으로 성립하는 과정"**

<br/>

---

# 상속 예제 - 동물 1

<br/>

```python
class Animal:
    def __init__(self, legs: int, name: str):
        self.legs: int = legs
        self.name: str = name
    
    def info(self):
        print(self.name, "은", self.legs, "개의 다리를 가집니다.")

class Dog(Animal):
    def walk(self):
        print(self.name, "이 걷습니다.")

class Bird(Animal):
    def fly(self):
        print(self.name, "이 하늘을 날아갑니다.")
```

---

# 상속 예제 - 동물 2

<br/>

```python
eagle = Bird(2, "독수리")
poodle = Dog(4, "푸들")
eagle.fly()
poodle.walk()
```

---

# 4. 다형성 (Polymorphism)

---

# 다형성 (Polymorphism)

<br/>

> **"서로 다른 클래스의 객체가 같은 동작 수행 명령을 받았을 때, 각자의 특성에 맞는 방식으로 동작하는 것"**

<br/>

---

# 다형성 예제 1

<br/>

```python
class Operator:
    def calculate(self, a, b):
        pass    # 함수의 내용을 비워두는 키워드

class Add(Operator):
    def calculate(self, a, b):
        return a + b

class Multiply(Operator):
    def calculate(self, a, b):
        return a * b
```

---

# 다형성 예제 2

<br/>

```python
add: Operator = Add()
mul: Operator = Multiply()

print(add.calculate(5, 6))
print(mul.calculate(5, 6))
```

---

# 요약

1. 추상화 (Abstraction)
    객체들 간에 공통되는 속성이나 동작을 하나로 추출해내는 작업
2. 캡슐화 (Encapsulation)
    정보 은닉화를 통해 높은 응집도, 낮은 결합도를 유지할 수 있도록 설계하는 것
3. 상속 (Inheritance)
    여러 개체들이 지닌 공통된 특성을 부각시켜 하나의 개념이나 법칙으로 성립하는 과정
4. 다형성 (Polymorphism)
    서로 다른 클래스의 객체가 같은 동작 수행 명령을 받았을 때, 각자의 특성에 맞는 방식으로 동작하는 것

---

# 강의를 들어줘서 고마워요 :wink:
