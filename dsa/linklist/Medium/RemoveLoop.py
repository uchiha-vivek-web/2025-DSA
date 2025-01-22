class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL : 
    def __init__(self,start=None):
        self.start=start
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def print(self):
        temp=self.start
        while temp is not None :
            print(temp.item,end=' ')
            temp=temp.next
def removeLoop(head:SLL):
    nodeSet = set()
    temp=None
    while head : 
        if head in nodeSet:
            temp.next=None
            return
        nodeSet.add(head)
        temp=head
        head=head.next

mylist=SLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.print()
removeLoop(mylist.start)
mylist.print()