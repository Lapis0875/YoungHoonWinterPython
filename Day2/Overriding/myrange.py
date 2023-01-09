class MyRange:
    def __init__(self, start: int, end: int, step: int):
        self.end: int = end
        self.step: int = step
        self.index: int = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == self.end:
            raise StopIteration()
        v = self.index
        self.index += 1
        return v

for i in range(5):
    print(i)
for i in MyRange(0, 5, 1):
    print(i)