class Node:
    def __init__(self , data = None , next = None):
        self.data = data
        self.last = None
        self.next = None

class Queue:
    def __init__(self, *data):
        self.front = None
        self.rear = None
        self.size = 0
        for value in data:
            self.enQueue(value)

    def enQueue(self , data):
        self.lastNode = self.front #temporarily stores the old front node
        self.front = Node(data , self.front) #creates a new node and immediately makes it the new front node
        #connects old front node back to the new front
        if self.lastNode:
            self.lastNode.setLast(self.front)
        self.size += 1

    def queueRear(self):
        if self.rear is None:
            raise IndexError("Empty queue")
        return self.rear.data
    
    def queueFront(self):
        if self.front is None:
            raise IndexError("Empty queue")
        return self.front.data
    
    def deQueue(self):
        if self.rear is None:
            raise IndexError("Empty queue")
        dequeue_data = self.rear.data
        self.rear = self.rear.last
        self.size -= 1
        return dequeue_data
    
    def display(self):
        if self.front is None:
            print("Queue([])")
            return
        
        current = self.front()
        print("Front --> " , end = " ")

        while current:
            print(current.data, end="")
            if current.next:
                print(" → ", end="")
            current = current.next
        print(" ← Rear")
    
    def size(self):
        return self.size
    
que = Queue(10,20,30,40)

que.enQueue(10)
que.enQueue(20)
que.enQueue(30)
que.enQueue(40)

que.display()
# Output: Front → 10 → 20 → 30 → 40 ← Rear

print("Front:", que.queueFront())   # 10
print("Rear:", que.queueRear())     # 40

que.deQueue()
que.display()
# Output: Front → 20 → 30 → 40 ← Rear