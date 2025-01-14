class Stack :
    def __init__(self):
        self.stack=[]
    def push(self,nums:int)->None :
        self.stack.append(nums)
    def isEmpty(self)-> bool :
        return len(self.stack)==0
    def size(self)-> int :
        return len(self.stack)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else :
            print('Stack is Empty')
            return
    def peek(self):
        if self.isEmpty():
            return self.stack[-1]
        else :
            print('Stack is Empty')
            return
    
    def reverse_array(self,nums:list[int]) :
        for num in nums :
            self.push(num)
        dummy_list=[]
        while not self.isEmpty():
            print(self.pop())
         
    
sol=Stack()
nums=[10,20,30,40,50]
ans = sol.reverse_array(nums)
print(ans)