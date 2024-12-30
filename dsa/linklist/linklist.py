"""  Making a Node """

class Node : 
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
        
class SLL :
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None :
                temp=temp.next
            temp.next=n
        else :
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None :
            if temp.item==data:
                return data
                
            temp=temp.next
        return None
        
        
    def insert_after(self,temp,data):
        if temp is not None :
            n=Node(data,temp.next)
            
    
    def print_list(self):
        temp=self.start
        while temp is not None :
            print(temp.item,end=' ')
            temp=temp.next
        
        
        
        
        

mylist = SLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.print_list()




