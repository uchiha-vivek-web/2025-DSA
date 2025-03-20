class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return data
            temp = temp.next
        return None

    def delete_node(self, data):
        if self.isEmpty():
            print("List is empty")
            return

        # If head node is to be deleted
        if self.start.item == data:
            self.start = self.start.next
            return

        temp = self.start
        prev = None

        # Traverse to find the node to delete
        while temp is not None and temp.item != data:
            prev = temp
            temp = temp.next

        # If node was not found
        if temp is None:
            print("Node not found")
            return

        # Unlink the node
        prev.next = temp.next

    """Length of linklist """
    def length_linklist(self):
        count=0
        temp=self.start
        while temp is not None :
            temp=temp.next 
            count+=1
        return count


    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end="->")
            temp = temp.next
        print("None")


# Example Usage
mylist = SLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
print(mylist.length_linklist())
print("Before deletion:")
mylist.print_list()

mylist.delete_node(20)

print("After deletion:")
mylist.print_list()
