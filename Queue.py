queue = [10,20,30,40]
def isEmpty(queue):
    if len(queue) == 0:
        return True
    else:
        return False
def enqueue(queue,item):
    if isEmpty(queue) == True:
        return "Overflow"
    else:
        queue.append(item)
        if len(queue) == 1:
            front=rear=0
        else:
            rear = len(queue)-1
def dequeue(queue):
    if isEmpty(queue) == True:
        return "Underflow"
    else:
        val = queue.pop(0)
        if len(queue)==0:
            front=rear=None
        return val
def Peek(queue):
    if isEmpty(queue):
        return "Underflow"
    else:
        front = 0
        return queue[front]
def Show(queue):
    if isEmpty(queue):
        print("Sorry No items in Stack")
    else:
        print("(Front)",end=' ')
        front=0
        rear=len(queue)-1
        i=front
        while(i<=rear):
            print(queue[i],"<=",end=' ')
            i=i+1
        print()
queue = [10,20,30,40]
front = rear = None
enqueue(queue,50)
enqueue(queue,60)
Show(queue)
dequeue(queue)
print(Peek(queue))
Show(queue)
