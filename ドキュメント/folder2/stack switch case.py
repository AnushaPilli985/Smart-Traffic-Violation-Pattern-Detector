stack=[]
while True:
    print("operations")
    print("1.push operation")
    print("2.pop operation")
    print("3.peek operation")
    print("4.is empty operation")

    choice=int(input("enter an option"))
    if choice==1:
        item=int(input("enter the number to be pushed:"))
        stack.append(item)
        print(stack)
    elif choice==2:
        if stack:
             item=int(input("enter the number to be delete:")) 
             stack.pop(item)
             print(stack)

        else:
            print("stack is empty,can't pop")
    elif choice==3:
        if stack:
            peek=stack[-1]
            print(peek)
        else:
            print("stack is empty")
    elif choice==4:
        if not stack:
            print("stack is empty")
        else:
            print("stack is not empty")
    else:
        print("enter valid option")                


