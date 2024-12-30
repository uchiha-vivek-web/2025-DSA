""" Reversing a Linkedlist """

class Node :
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL :
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        """Make a node"""
        n = Node(data,self.start)
        self.start = n
    def print_last(self):
        temp = self.start
        while temp is not None :
            print(temp.item,end=' ')
            temp=temp.next
    
    def reverse(self):
        prev=None
        current=self.start
        while current is not None :
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.start=prev


mylist= SLL()
mylist.insert_at_start(5)
mylist.insert_at_start(4)
mylist.insert_at_start(3)
mylist.insert_at_start(2)
mylist.insert_at_start(1)
mylist.print_last()
print('')
mylist.reverse()
mylist.print_last()