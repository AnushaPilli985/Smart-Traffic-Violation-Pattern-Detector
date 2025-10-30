queue=[]
def enqueue():
    ele=int(input("enter a elelment:"))
    queue.append(ele)
    print("element entered ",queue)
def dequeue():
    if not queue:
        print("queue is empty!")
    else:
        e= queue.pop(0)
        print("element is deleted ",e)
def display():
    print(queue)
while True:
    print("enter a choice:")
    choice=int(input())

    if choice==1:
        print(enqueue())
    elif choice==2:
        print(dequeue())
    elif choice==3:
        print(display())
    else:
        break        

                












