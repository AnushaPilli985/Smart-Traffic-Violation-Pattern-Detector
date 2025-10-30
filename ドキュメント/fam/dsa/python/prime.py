n=int(input("enter a  number:"))
flag=False
if n==1:
    print("1 is not a prime number")
elif n>1:
    for i in range(2,n):
        if (n%i==0):
            flag=True
            break
if flag:
    print(f"{n} is a not prime number")
else:
    print(f"{n} is a prime number") 
        
