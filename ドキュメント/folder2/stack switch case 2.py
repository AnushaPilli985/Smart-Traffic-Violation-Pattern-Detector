stack = []
while True:
    print("\noperations")
    print("1. push operation")
    print("2. pop operation")
    print("3. peek operation")
    print("4. is empty operation")

    choice = int(input("enter an option: "))
    if choice == 1:
        item = int(input("enter the number to be pushed: "))
        stack.append(item)
        print(stack)

    elif choice == 2:
        if stack:
            stack.pop()
            print(stack)
        else:
            print("stack is empty, cannot pop")

    elif choice == 3:
        if stack:
            peek = stack[-1]
            print("Top element is:", peek)
        else:
            print("stack is empty, no peek available")

    elif choice == 4:
        if not stack:
            print("stack is empty")
        else:
            print("stack is not empty")

    else:
        print("enter valid option")
