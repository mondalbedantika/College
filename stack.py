class Node:
    def __init__(self , data = None , next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self , *data):
        self.head = None
        self._size = 0
        if data:
            for item in data:
                self.push(item)

    def push(self , data):
        new_node = Node(data , self.head)
        self.head = new_node
        self._size += 1
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Empty Stack")
        popped_data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return popped_data
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.head.data
    
    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self._size
    
    def clear(self):
        self.head = None
        self._size = 0

    def display(self):
        if self.is_empty():
            return "Stack ([])"
        
        items = []
        current = self.head
        while current:
            print(f"  {current.data}")
            current = current.next

    def __len__(self):
        return self._size

    def __bool__(self):
        return not self.is_empty()

stack = Stack(10,20,30,40)
print("Original Stack : ")
stack.display()

stack.push(70)
stack.push(80)
stack.push(90)
print("Stack after pushing new elements : ")
stack.display()

stack.pop()
print("Stack after popping last elemet : ")
stack.display()

stack.peek()