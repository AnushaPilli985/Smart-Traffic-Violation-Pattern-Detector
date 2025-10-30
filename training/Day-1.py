
for i in range(9):
    print(i)

i=1
while i<=50:
    print(i) 
    i+=1

#sum of n numbers using for loop
sum=0
for i in range(1,51):
    sum+=i
print(sum)

#sum of n numbers using while
sum=0
i=0
while i<=50:
    sum+=i
    i+=1
print(sum)

#sum of even numbers
sum=0
for i in range(101):
    if i%2==0:
        sum+=i
print(sum)

#sum of even numbers using while 
sum=0
i=0
while i<=100:
    if i%2==0:
        sum+=i
    i+=1
print(sum)

#100 numbers
i=0
while i<=50:
    if i%2!=0:
        print(i,end=" ")
    i+=1
        
#sum of odd numbers using for loop
sum=0
for i in range(100):
    if i%2!=0:
        sum+=i
print(sum)

#sum of odd numbers using while loop
sum=0
i=0
while i<=100:
    if i%2!=0:
        sum+=i
    i+=1
print(sum)


#sum of odd and even sum
sum_even=0
sum_odd=0
for i in range(100):
    if i%2==0:
        sum_even+=i
    
    else:
         sum_odd+=i  
print(sum_even)
print(sum_odd)
print("diff of odd sum and even sum:",sum_odd-sum_even)
print("diff of odd sum and even sum:",sum_even-sum_odd)



#numbers divisible by 3 and 5
for i in range(100):
    if i%3==0 and i%5==0:
        print(i)

#multiplication of table 2
for i in range(11):
    # print(f"2 * {i} = {2*i}")
    print("2 * ",i ,"=",2*i)



print(complex(5,6))
for i in range(20,0,-5):
    print(i)

for i in range(1,10):
   
    if i==5:
        break  
    print(i)


#gcd of number
a=15
b=20
res=min(15,20)
for i in range(1,res,-1):
    if a%i==0 and b%i==0:
        print(i)
        break
  
        
import math
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=a+b
d=a//b
print(c)
print(math.floor(d))
print(math.floor(8.3435))
print(math.ceil(8.3435))

#logical operators
print("and or")

#comparsion operators
a=6
b=9
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)

#arithemtic operators
a=int(input("enter a value:"))
b=int(input("enter b value:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #debugging
print(a%b)
print(a**b)

#grade
marks=int(input("enter marks:"))
if marks>=90:
    print("Grade A")
elif marks<90 and marks>=80:
    print("Grade B")
elif marks<80 and marks >=70:
    print("Grade C")
elif marks<=70:
    print("Fail")
else:
    print("enter valid marks")

#swap numbers
a=8
b=9
print("before swapping:",a,b)
a,b=b,a
print("after swapping:",a,b)

#swap numbers
a=1
b=7
a=a+b
b=a-b
a=a-b

print(a)
print(b)

#swapping using ex-or symbol
a=8
b=6
a=a^b
b=a^b
a=a^b

print(a,b)

#int to binary
n=int(input("enter a number:"))
bin_id=""
while n>0:
    rem=n%2
    bin_id=str(rem)+bin_id
    n=n//2
print(bin_id) 


#binary to integer
n=input("enter a bin num:")
decimal=0
for i in n:
    if i not in ('0','1'):
        print("invalid")
        exit()
decimal=decimal*2 + i
print(decimal)        


# *****
# *****
# *****
# *****
# *****
for i in range(5):
    print(5 * "*")


#      *
#     **
#    ***
#   ****
n=int(input("enter num:"))
for i in range(n):
    print((n-i) * " ", i* "*")
    
for i in range(6,0,-1):
    print((6-i) * " ", i* "*")


#      *  
#     ***  
#    *****  
#   *******  
#  *********  
#  *********  
#   *******  
#    *****  
#     ***  
#      *  
for i in range(5):
    print((5-i-1) * " ",(2*i+1) * "*"," ")
for i in range(5,0,-1):
    print((5-i) * " ",(2*i-1) * "*"," ")



    
