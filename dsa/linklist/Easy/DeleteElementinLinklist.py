class Node :
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL :
    def __init__(self,start=None):
        self.start=start
    def isEmpty(self):
        return self.start==None
    def insertAtStart(self,data):
        n=Node(data,self.start)
        self.start=n
    def print(self):
        temp=self.start
        while temp is not None : 
            print(temp.item,end=' ')
            temp=temp.next
    def deleteItemFromFront(self):
        if self.start is None :
            print('List is empty , Nothing to print ! ')
            return
        self.start = self.start.next
    def deleteItemAtIndex(self,index):
        if self.start is  None :
            print('List is empty , Nothing to print ! ')
            return
        if index==0 :
            self.start=self.start.next
            return
        temp=self.start
        for i in range(index-1):
            if temp is None or temp.next is None:
                print('Index out of bounds')
                return
            temp=temp.next
            if temp.next is None :
                print('Index out of bound')
                return
            temp.next=temp.next.next









mySLL = SLL()
mySLL.insertAtStart(10)
mySLL.insertAtStart(20)
mySLL.insertAtStart(30)
mySLL.insertAtStart(40)
mySLL.print()
mySLL.deleteItemAtIndex(1)
print()
mySLL.print()
# mySLL.deleteItemFromFront(20)
# print()
# mySLL.print()