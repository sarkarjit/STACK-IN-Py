def push(myStack, value, leng):
    if len(myStack)==leng:
        print("Stack Overflow")
    else:
        myStack.append(value)

def pop(myStack):
    if len(myStack)==0:
        print("Stack Underflow")
    else:
        myStack.pop()

def display(myStack):
    myStack.reverse()
    for i in range(0, len(myStack)):
        print(myStack[i])

def isEmpty(myStack):
    if myStack==0:
        print("Underflow")
    else:
        print("Not Empty")
def isFull(myStack, leng):
    if len(myStack)==leng:
        print("Overflow")
    else:
        print("Not Full")

myStack=[]

leng=int(input("Enter your size of the stack"))

print("Enter your elements")
for i in range(0, leng):
    val = int(input())
    push(myStack, val, leng)

pop(myStack)

display(myStack)