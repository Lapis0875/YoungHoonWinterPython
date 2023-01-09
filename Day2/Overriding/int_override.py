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