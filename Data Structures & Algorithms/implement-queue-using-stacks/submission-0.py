class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        if not self.empty():
            first_item = self.items[0]
            self.items = self.items[1:]
            return first_item

    def peek(self) -> int:
        return self.items[0]
        

    def empty(self) -> bool:
        return not self.items
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()