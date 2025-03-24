""" Implement stack using queue """
from collections import deque

class StackUsingQueue:
    def __init__(self):
        self.queue=deque()
    
    def push(self,num):
        self.queue.append(num)
        for _ in range(len(self.queue) -1):
            self.queue.append(self.queue.popleft())
    
    def isEmpty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)

    def pop(self):
        if not self.isEmpty():
            return self.queue.popleft()
        else :
            print('Stack is empty')
            return None
        
    def peek(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            print('Stack is empty')
            return
        


stack=StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size())  # Output: 3
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
print(stack.peek())  # Output: 2