num=int(input("enter the number:"))
count=0
if num==0 and num==1:
    print("number is a prime number")
for i in range(2,num):
    if (num%i)==0:
        count+=1
if count==2:
    print(f"{num} is not a prime number")   
else:
    print(f"{num} is  prime number")         
