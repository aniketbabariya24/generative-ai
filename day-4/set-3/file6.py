# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None"

from collections import deque

class Stack:
    def __init__(self):
        self.queue = deque()

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0



stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop()) 
stack.push(3)
print(stack.pop())  
print(stack.pop())  
print(stack.pop()) 
