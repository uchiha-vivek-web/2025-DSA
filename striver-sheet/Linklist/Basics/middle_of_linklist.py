class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def findLength(self):
        count = 0
        temp = self.start
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def middleElement(self):
        length = self.findLength()
        mid_index = length // 2  # Get the middle index (0-based)

        temp = self.start
        for _ in range(mid_index):  # Traverse to the middle element
            temp = temp.next

        if temp:
            print(f"Middle element is: {temp.data}")
        else:
            print("List is empty")

    def insert(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    
    def findMiddleElementByFloydMethod(self):
        slow=self.start
        fast=self.start
        while fast and fast.next and slow:
            fast=fast.next.next
            slow=slow.next
        return slow


# Example Usage
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.findMiddleElementByFloydMethod()
# ll.middleElement()  # Output: Middle element is: 3
