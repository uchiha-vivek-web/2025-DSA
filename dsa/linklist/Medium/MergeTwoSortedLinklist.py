class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def print(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

def merge_sorted_lists(list1: SLL, list2: SLL) -> SLL:
    dummy = Node()  # Temporary node to simplify logic
    tail = dummy

    # Pointers to the start of both lists
    l1 = list1.start
    l2 = list2.start

    # Merge the two lists
    while l1 is not None and l2 is not None:
        if l1.item < l2.item:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Append any remaining elements
    if l1 is not None:
        tail.next = l1
    elif l2 is not None:
        tail.next = l2

    # Return the merged list starting from the first real node
    merged_list = SLL(dummy.next)
    return merged_list

# Example Usage
list1 = SLL()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = SLL()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

print("List 1:")
list1.print()
print("List 2:")
list2.print()

merged_list = merge_sorted_lists(list1, list2)
print("Merged List:")
merged_list.print()
