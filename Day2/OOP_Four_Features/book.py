class Book:
    def __init__(self, name: str):
        self.name: str = name
    
    def info(self):
        print(self.name)
    
    def borrow(self, who: str):
        print(who, "가", self.name, "을(를) 빌렸습니다.")

book1 = Book("신데렐라")
book2 = Book("헨젤과 그레텔")

book1.info()            # 신데렐라
book2.info()            # 헨젤과 그레텔

book1.borrow("철수")    # 철수 가 신데렐라 을(를) 빌렸습니다.
book2.borrow("영희")    # 영희 가 헨젤과 그레텔 을(를) 빌렸습니다.