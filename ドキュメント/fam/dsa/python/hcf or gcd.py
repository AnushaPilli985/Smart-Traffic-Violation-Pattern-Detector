#import math

#print(math.gcd(4,18))
def compute_HCF(a,b):
    if b==0:
       return a 
    else:
       return compute_HCF(b,a%b)
print(compute_HCF(4,18))    
    

