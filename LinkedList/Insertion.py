class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begin(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self,value):
        if self.head is None:
            return "Empty Linked List"
        new_node = Node(value)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.next = None

    def insert_at_position(self,value,pos):
        if self.head is None:
            return "Empty Linked List"
        if pos < 0:
            return "Invalid POsition"
        new_node = Node(value)
        temp = self.head
        count = 0
        while temp.next != None and count < pos - 1:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data,end=" --> ")
            temp = temp.next
        print("None")

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

ll = LinkedList()
ll.head = node1
ll.insert_at_begin(5)
ll.insert_at_position(25,3)
ll.insert_at_end(55)
ll.display()