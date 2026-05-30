class Stack:
    def __init__(self):
        self._items = []
    def push(self, data):
        self._items.append(data)
    def size(self):
        return len(self._items)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(20)
stack.push(30)

print(f"Stack size: {stack.size()}")