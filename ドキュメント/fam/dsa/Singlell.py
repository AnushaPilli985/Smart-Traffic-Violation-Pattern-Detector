class node:
    def __init__(self,data):
        self.data=data
        self.reference=None
class Linkedlist:         
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is none:
            print("ll is empty")
        else:
            n=self.head
            while n is not none:
                print(n.data)
                n=n.reference     

 