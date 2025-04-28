
class Heap:
    def __init__(self,capacity):
        self.storage = [0]*capacity
        self.capacity = capacity
        self.size=0

    def getParentIndex(self,index):
        idx:int = (index-1)//2
        return idx
    
    def getLeftChildIndex(self,index):
        idx:int = 2*index+1
        return idx

    def getRightChildIndex(self,index):
        idx:int = 2*index+2
        return idx
    
    def hasParent(self,index):
        return self.getParentIndex(index)>=0
    
    def hasLeftChild(self,index):
        return self.getLeftChildIndex(index)<self.size
    
    def hasRightChild(self,index):
        return self.getRightChildIndex(index)<self.size
    

    # getting actual data
    def parent(self,index):
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self,index):
        return self.storage[self.getLeftChildIndex(index)]
    
    def rightChild(self,index):
        return self.getLeftChildIndex[self.getRightChildIndex(index)]
    
    def isFull(self):
        return self.size==self.capacity
    
    def swap(self,index1,index2):
        temp=self.storage[index1]
        self.storage[index1]=self.storage[index2]
        self.storage[index2]=temp

    def insert(self,data):
        if(self.isFull()):
            raise ('Heap is Full !')
        self.storage[self.size]=data
        self.size+=1
        self.heapifyUp()

    """recursive implementation"""
    def insertr(self,data):
        if(self.isFull()):
            raise ('Heap is Full !')
        self.storage[self.size]=data
        self.size+=1
        self.heapifyUp(self.size-1)
    
    def heapifyUp(self):
        index=self.size-1
        while(self.hasParent(index) and self.parent(index)>self.storage[index]):
            self.swap(self.getParentIndex(index),index)
            index= self.getParentIndex(index)

    """recursive implementation"""
    def heapifyUpr(self,index):
        if(self.hasParent(index) and self.parent(index)>self.storage[index]):
            self.swap(self.getParentIndex(index),index)
            self.heapifyUpr(self.getParentIndex(index))