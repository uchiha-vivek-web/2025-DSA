class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None

    def insert(self, data):
        """Make a Node"""
        n = Node(data, self.start)
        self.start = n

    def print(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()

    @staticmethod
    def mergeTwoLists(list1: Node, list2: Node):
        dummy = Node()
        cur = dummy
        while list1 and list2:
            if list1.item > list2.item:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return dummy.next

# Create two sorted linked lists
list1 = SLL()
list2 = SLL()

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
list1.insert(4)
list1.insert(2)
list1.insert(1)
list2.insert(4)
list2.insert(3)
list2.insert(1)

print("List 1:")
list1.print()

print("List 2:")
list2.print()

# Merge the two lists
merged_head = SLL.mergeTwoLists(list1.start, list2.start)

# Create a new SLL for the merged list
merged_list = SLL(merged_head)

print("Merged List:")
merged_list.print()
