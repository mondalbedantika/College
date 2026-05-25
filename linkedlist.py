class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self , data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def update(self , value , index):
        if self.head is None:
            print("List is empty")
            return
        if index < 0:
            print("Invalid Index")
            return
        temp = self.head
        position = 0

        while temp is not None and position != index:
            temp = temp.next
            position += 1

        if temp is None:
            print(f"Index {index} is out of range")
        else:
            temp.data = value
            print(f"Updated index {index} to {value}")

    def delete_at_begin(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    def delete_last_node(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current is not None:
            print(current.data , end = " ---> ")
            current = current.next
        print("None")


nodes = [Node(i) for i in range(1,11)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i+1]

ll = LinkedList()
ll.head = nodes[0]
print("Original List : ")
ll.display()
ll.insert_at_begin(0)
ll.insert_at_end(25)
print("\nAfter insertions:")
ll.display()

ll.update(28,7)
print("\nAfter Updations : ")
ll.display()