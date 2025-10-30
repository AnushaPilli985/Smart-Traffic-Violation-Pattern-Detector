class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.stack.pop()

    def isempty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.stack[-1]

    def display(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack elements:", self.stack)

    def __str__(self):
        return f"Stack({self.stack})"
