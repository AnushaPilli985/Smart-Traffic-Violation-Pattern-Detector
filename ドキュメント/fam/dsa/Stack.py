class stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if not self.stack:
            print("stack is empty")
           
        else:
            return self.stack.pop()    
    def isempty(self):
        return len(self.stack)==0
    
    def peek(self):
        if self.isempty():
            return len(self.stack)==0
        else:
            return self.stack[-1]
    
    def display(self):
        if self.isempty():
            return "stack is empty"
        else:
            print("stack elements:",self.stack)
        
s=stack()
s.push(9)
s.push(5)
s.push(4)
s.pop()
s.push(3)

s.pop()
s.pop()
s.pop()
s.pop()

s.display()
s.display()


           
        
