def factorial_cal(n):
    if n<=0:
        return 1
    else:
        return n*factorial_cal(n-1)
print(factorial_cal(7))    
    
