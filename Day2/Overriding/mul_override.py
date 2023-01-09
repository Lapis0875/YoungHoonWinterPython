class IntBox:
    def __init__(self, value: int):
        self.value: int = value
    
    def __str__(self) -> str:
        return "IntBox(" + str(self.value) + ")"
    
    def __mul__(self, other):
        if isinstance(other, IntBox):
            # 우항도 NumberBox의 인스턴스일 때
            return IntBox(self.value * other.value)
        elif isinstance(other, int):
            # 우항이 int형 값일 때
            return IntBox(self.value * other)
        # 정의되지 않은 연산은 반드시 NotImplemented 을 반환해야 해요.
        return NotImplemented

a = IntBox(3)
b = IntBox(4)
c = 5
d = "6"

print(a * b)    # IntBox(12)
print(a * c)    # IntBox(15)
# TypeError: unsupported operand type(s) for *: 'IntBox' and 'str'
print(a * d)  