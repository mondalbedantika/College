class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def delete_at_begin(self):
        if self.head is None:
            return "Empty Linked List"
        self.head = self.head.next
        
    def delete_at_end(self):
        if self.head is None:
            return "Empty Linked List"
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def delete_at_position(self,pos):
        if pos == 1:
            self.delete_at_begin()
        if pos < 0:
            return "Invalid Position"
        temp = self.head
        count = 1 #starting index = 1
        while temp.next is not None and count == pos-1:
            temp = temp.next
            count += 1
        temp.next = temp.next.next

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
ll.delete_at_begin()
ll.delete_at_end()
ll.delete_at_position(3)
ll.display()