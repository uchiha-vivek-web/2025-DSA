"""1-> Make a custom stack"""
"""2-> Try to reverse the string."""

class Stack :
    def __init__(self):
        self.stack=[]
    """Pushing string character"""
    def push(self,character:str) :
        self.stack.append(character)
    def isEmpty(self)->bool :
        return len(self.stack)==0
    def size(self)-> int :
        return len(self.stack)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print('Stack is Empty')
            return
    def reverse(self,character:str):
        for ch in character :
            self.push(ch)
        reversed_string = ''
        while not self.isEmpty():
            reversed_string+=self.pop()
        return reversed_string
        
sol=Stack()
character = 'abc'
ans = sol.reverse(character)
print(ans)