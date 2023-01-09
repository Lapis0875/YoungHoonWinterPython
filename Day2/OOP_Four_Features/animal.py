class Animal:
    def __init__(self, legs: int, name: str):
        self.legs: int = legs
        self.name: str = name
    
    def info(self):
        print(self.name, "은", self.legs, "개의 다리를 가집니다.")

class Dog(Animal):
    def walk(self):
        print(self.name, "가 걷습니다.")

class Bird(Animal):
    def fly(self):
        print(self.name, "이 하늘을 날아갑니다.")

eagle = Bird(2, "독수리")
poodle = Dog(4, "푸들")
eagle.fly()                 # 독수리 가 하늘을 날아갑니다.
poodle.walk()               # 푸들 이 걷습니다.