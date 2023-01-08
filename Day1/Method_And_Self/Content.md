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
    --color-fg-default: #c9d1d9;ㄴㄴㄴㄴㄴㄴㄴㄴㄴㄴ
    --color-canvas-default: #0d1117;
  }
</style>

# 메소드와 self

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

# 1. 메소드란?

---

# 객체

<br/>

소프트웨어 세계에 구현할 대상(개념)으로, `속성(attribute)`과 `행위(behavior)`를 가져요.

---

# 메소드

<br/>

객체의 `행위`는 메소드로 표현해요. 이전에 배운 함수와 같지만, 함수가 클래스 내부에 선언되어 객체의 동작을 표현할 경우 메소드라고 불러요.

---

# 메소드 호출하기

<br/>

```python
class Book:
    def __init__(self, name: str, category: str):
        # 객체가 가지는 속성들이에요.
        self.name: str = name
        self.category: str = category
    
    def info(self):
        print(self.category, ":", self.name)

# 객체가 실제로 구현된, 인스턴스들이에요.
cinderella = Book("신데렐라", "동화")
cinderella.info()   # 메소드를 호출해요.
```

<br/>

---

# self는 어디로 갔을까요?

<br/>

```python
    ...
    def info(self):
        print(self.category, ":", self.name)
```

<br/>

---

# 2. 메소드의 특수한 인자, self

---

# self

<br/>

self는 메소드 내에서 인스턴스 자신을 가리켜요. self를 통해, 인스턴스에 저장된 `속성`값들을 가져올 수 있어요.

<br/>

```python
    ...
    def info(self):
        print(self.category, ":", self.name)
```

<br/>

---

# self 사용해보기

<br/>

```python
class Box:
    def __init__(self, name: str):
        self.name: str = name
        self.content = None

    def info(self):
        """상자 내부의 내용물을 확인해요."""
        t = type(self.content)
        if t is None:
            print(self.name, "상자는 지금 비어있어요.")
        else:
            print(self.name, "상자 안에는", t, "자료형의 값이 있어요.")
```

<br/>

---

# self 사용해보기

<br/>

```python
    
    def open(self):
        """상자를 개봉해요. 상자 내부의 내용물을 꺼내요."""
        c = self.content
        self.content = None
        return c
    
    def wrap(self, content):
        """상자를 새 내용물을 넣고 포장해요. 인자로 받은 값을 저장해요."""
        self.content = content
```

<br/>

---

# self 사용해보기

<br/>

```python
box1 = Box("1번")
box1.info()             # 1번 상자는 지금 비어있어요.
box1.wrap(42)
box1.info()             # 1번 상자 안에는 int 자료형의 값이 있어요.
print(box1.open())      # 42
box1.info()             # 1번 상자는 지금 비어있어요.
```

<br/>

---

# 요약

<br/>

1. 메소드
    객체의 `행위`를 표현하는 함수를 메소드라고 불러요. 함수와 선언 방식은 같으나, 첫 번째 인자는 반드시 self를 받아요.
2. self
   메소드 내에서 인스턴스 자신을 가리키는 인자에요. 인스턴스의 메소드 호출 시에는 누락되지만, 메소드 내부에 전달돼요.

---

# 강의를 들어줘서 고마워요 :wink:
