class Stack:
    def __init__(self,stek: list):
        self.stek = stek


    def is_empty(self) -> bool:
        if not self.stek:
            flag = True
        else:
            flag = False     
        return flag
    def push(self,num):
        self.stek.append(num)

    def pop(self):
        up_item = self.stek.pop()
        return up_item

    def peek(self):
        return self.stek[-1]

    def size(self) -> int:
        return len(self.stek) 