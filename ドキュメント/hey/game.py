import random 
true_number=random.randint(1,100)
true_number=int(input("Enter a number between 1 and 100:"))
guess_number=int(input("Enter a number between 1 and 100:"))
if true_number==guess_number:
    print("you guess is right")
elif true_number<guess_number:
    print("your guess is less than true_number,please try again")
    guess_number=int(input("Enter a number between 1 and 100:"))
elif true_number>guess_number:
     print("your guess is greater  than true_number,please try again")

         