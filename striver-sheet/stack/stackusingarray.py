"""implement stack using array"""


class Stack :
    def __init__(self):
        self.stack=[]
    def push(self,num):
        self.stack.append(num)
    def isEmpty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
    def pop(self):
        if not self.isEmpty():
            self.stack.pop()
        else:
            print('Stack is Empty')
            return None
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print('Stack is Empty')
            return None

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size())