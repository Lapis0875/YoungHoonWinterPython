class Box:
    """
    상자.
    비어있으면 거짓, 내용물이 있으면 참.
    """
    def __init__(self):
        self.content = None
    
    def wrap(self, content):
        self.content = content
    
    def unwrap(self):
        c = self.content
        self.content = None
        return c

    def __bool__(self) -> int:
        return self.content != None

b = Box()
if not b:
    print("현재 상자가 비어있어요.")
    
b.wrap(42)
if b:
    print("현재 상자에는", b.content,"가 들어있어요.")

b.unwrap()
if not b:
    print("현재 상자가 비어있어요.")