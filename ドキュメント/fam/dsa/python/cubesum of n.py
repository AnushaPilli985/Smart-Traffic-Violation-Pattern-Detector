def cube_sum_of_natural_number(n):
    if n<=0:
        return 0
    else:
        total=0
        for i in range(1,n+1):
            cube=i**3
            total+=cube
        return total
n=int(input("enter a number:"))
result=cube_sum_of_natural_number(n)
print(result)        
     


