class Book:
    def __init__(self, name: str, category: str):
        self.name: str = name
        self.category: str = category

    def __str__(self) -> str:
        return "{제목:" + self.name + ",분류:" + self.category + "}"

print(Book("파이썬 프로그래밍", "전공서"))