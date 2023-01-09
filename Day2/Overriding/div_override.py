class FloatBox:
    def __init__(self, content: float):
        self.value: float = content
    
    def __str__(self) -> str:
        return "FloatBox(" + str(self.value) + ")"
    
    def __add__(self, other):
        if isinstance(other, FloatBox):
            # 우항도 NumberBox의 인스턴스일 때
            return FloatBox(self.value + other.value)
        elif isinstance(other, int):
            # 우항이 int형 값일 때
            return FloatBox(self.value + other)
        # 정의되지 않은 연산은 반드시 NotImplemented 을 반환해야 해요.
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, FloatBox):
            # 우항도 NumberBox의 인스턴스일 때
            return FloatBox(self.value - other.value)
        elif isinstance(other, int):
            # 우항이 int형 값일 때
            return FloatBox(self.value - other)
        # 정의되지 않은 연산은 반드시 NotImplemented 을 반환해야 해요.
        return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, FloatBox):
            # 우항도 NumberBox의 인스턴스일 때
            return FloatBox(self.value * other.value)
        elif isinstance(other, int):
            # 우항이 int형 값일 때
            return FloatBox(self.value * other)
        # 정의되지 않은 연산은 반드시 NotImplemented 을 반환해야 해요.
        return NotImplemented
    
    def __truediv__(self, other):
        if isinstance(other, FloatBox):
            # 우항도 NumberBox의 인스턴스일 때
            return FloatBox(self.value / other.value)
        elif isinstance(other, (int, float)):
            # 우항이 int형 또는 float형 값일 때
            return FloatBox(self.value / other)
        # 정의되지 않은 연산은 반드시 NotImplemented 을 반환해야 해요.
        return NotImplemented

a = FloatBox(6)
b = FloatBox(3)
c = 2
d = "1"

print(a / b)    # FloatBox(2.0)
print(a / c)    # FloatBox(3.0)
# TypeError: unsupported operand type(s) for /: 'FloatBox' and 'str'
print(a / d)  