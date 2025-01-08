"""Implementing Queue using an Array"""
class Queue :
    def __init__(self):
        self.queue = []
    def isEmpty(self) -> bool :
        return len(self.queue)==0
    def isSize(self) -> int :
        return len(self.queue)
    def enqueue(self,element:int) -> None :
        self.queue.append(element)
    def deQueue(self)-> int : 
        if not self.isEmpty():
            return self.queue.pop(0)
        else :
            print('Queue is Empty')
            return None
    def front(self) -> int :
        if not self.isEmpty():
            return self.queue[0]
        else :
            print('Queue is Empty')
            return None
queue = Queue()

# Enqueue elements to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.isSize())