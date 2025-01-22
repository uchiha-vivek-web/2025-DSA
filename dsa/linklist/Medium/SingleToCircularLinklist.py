class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self) -> bool:
        return self.start is None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def print(self):
        if self.start is None:
            print("List is empty")
            return

        temp = self.start
        while True:
            print(temp.item, end=' ')
            temp = temp.next
            if temp == self.start:
                break
        print()

    def make_circular(self):
        if self.start is None:
            return  # No action needed for an empty list

        temp = self.start
        while temp.next is not None:  # Traverse to the last node
            temp = temp.next
        temp.next = self.start  # Point the last node to the start to make it circular

# Test the corrected code
mylist = SLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
print("Before making circular:")
mylist.print()
mylist.make_circular()
print("After making circular:")
mylist.print()
