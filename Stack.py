stack = [10,20,30,40]
def isEmpty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
def push(stack,item):
    if isEmpty(stack) == True:
        return "Overflow"
    else:
        stack.append(item)
        top = len(stack)-1
def pop(stack):
    if isEmpty(stack) == True:
        return "Underflow"
    else:
        val = stack.pop()
        if len(stack)==0:
            top=None
        else:
            top=len(stack)-1
        return val
def Peek(stack):
    if isEmpty(stack):
        return "Underflow"
    else:
        top=len(stack)-1
        return stack[top]
def Show(stack):
    if isEmpty(stack):
        print("Sorry No items in Stack")
    else:
        t=len(stack)-1
        print("(Top)",end=' ')
        while(t>=0):
            print(stack[t],"<==",end=' ')
            t=t-1
        print()
stack = [10,20,30,40]
push(stack,50)
push(stack,60)
Show(stack)
pop(stack)
print(Peek(stack))
Show(stack)