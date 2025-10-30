num=int(input("enter anumber:"))
i=1
factorial=1
if num<0:
    print("negativenumber")
elif num==0:
    print("factorail is 1")   
else:     
    for i in range(1,num+1):
        factorial=factorial*i
print("factorial of number",factorial)