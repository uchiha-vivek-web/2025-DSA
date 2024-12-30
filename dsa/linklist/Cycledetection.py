class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def print(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    def has_Cycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
        return False

# Create the linked list
mylist = SLL()
mylist.insert_at_start(5)
mylist.insert_at_start(4)
mylist.insert_at_start(3)
mylist.insert_at_start(2)
mylist.insert_at_start(1)
mylist.print()
print('')

# Check for a cycle
print(mylist.has_Cycle(mylist.start))
