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