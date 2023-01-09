class Operator:
    def calculate(self, a, b):
        pass    # 함수의 내용을 비워두는 키워드

class Add(Operator):
    def calculate(self, a, b):
        return a + b

class Multiply(Operator):
    def calculate(self, a, b):
        return a * b

add: Operator = Add()
mul: Operator = Multiply()

print(add.calculate(5, 6))
print(mul.calculate(5, 6))