def fibonacci_cal(n):
    if n<=1:
        return n
    else:
        return fibonacci_cal(n-1)+fibonacci_cal(n-2)
nterms=int(input("enter n value:"))
if nterms<=0:
    print("enter a positive value:") 
else:
    for i in range(nterms):
           print(fibonacci_cal(i))   
   
    
   

