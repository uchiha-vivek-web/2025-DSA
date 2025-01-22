class Node : 
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL :
    def __init__(self,start=None):
        self.start = start
    def isEmpty(self):
        return self.start==None
    def insertAtStart(self,data):
        n=Node(data,self.start)
        self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None :
            if temp.item==data :
                return data
            temp=temp.next
        return None
    def printlist(self):
        temp=self.start
        while temp is not None :
            print(temp.item,end='->')
            temp=temp.next
    """Search specific value and its frequency"""
    def frequency(self,data)-> int:
        temp=self.start
        count=0
        while temp is not None :
            if temp.item==data:
                count+=1
            temp=temp.next
        return count





mylist = SLL()
mylist.insertAtStart(10)
mylist.insertAtStart(10)
mylist.insertAtStart(30)
mylist.insertAtStart(10)
mylist.insertAtStart(20)
ans = mylist.frequency(10)
print(ans)
