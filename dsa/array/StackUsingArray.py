"""Implementing stack using Array"""
class Stack :
    def __init__(self):
        self.stack=[]
    def push(self,num:int) -> None :
        """Pushing the element to the top of the stack ."""
        self.stack.append(num)
    def isEmpty(self) -> bool :
        """Check if the list is empty"""
        return len(self.stack)==0
    def size(self) -> int :
        """Checks the length of the stack"""
        return len(self.stack)   
    def pop(self) -> int :
        if not self.isEmpty():
            return self.stack.pop()
        else :
            print('Stack is Empty ')
            return None
    def peek(self)-> int :
        if not self.isEmpty():
            return self.stack[-1]
        else :
            print('Stack is Empty')
            return None
        
stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size())
