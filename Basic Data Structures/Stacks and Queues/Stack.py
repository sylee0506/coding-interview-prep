class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()
    
    def peek(self): #return value of top element without removing from stack
        return self.stack[len(self.stack)-1]

    def isEmpty(self):
        return self.stack == [] #return boolean type

    def size(self):
        return len(self.stack)

"""
testing)
num1, num2 = input("input number:").split(' ')
num1 = int(num1); num2 = int(num2)
myStack = Stack()
myStack.push(num1)
myStack.push(num2)
print(myStack.size())
print(myStack.peek())
myStack.pop()
print(myStack.pop())
print(myStack.isEmpty())
"""


