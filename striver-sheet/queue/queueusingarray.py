""" Implement Queue using Array  """

class Queue :
    def __init__(self):
        self.queue=[]
    def enqueue(self,num):
        self.queue.append(num)
    def isEmpty(self):
        return len(self.queue)==0
    def size(self):
        return len(self.queue)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return None
    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            print('Queue is empty')
            return None
        

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.size())  # Output: 3
print(queue.dequeue())  # Output: 1
print(queue.front())  # Output: 2