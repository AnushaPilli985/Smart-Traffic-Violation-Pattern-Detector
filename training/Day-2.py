# selection control,repeative control(looping control),sequential control,jenkins control

a=4.7678
print(int(a))

#convert binary to integer base 2
a="1001"
print(int(a,2))
b=8
print(id(b))
print(id(a))
#int is mutable data type

# 1)program to print numbers 1 to 10 using for loop

for i in range(11):
    print(i,end=" ")

# 2)program t print numbers from 10 to 1 using while loop
i=10
while i>0:
    print(i)
    i-=1

# 3)program to print even numbers from 1 to 20 using while and for
for i in range(21):
    while i%2==0:
     print(i)
     i+=1

for i in range(2,21,2):
   print(i)
 
i=2
while i<=20:
   print(i,end=" ")
   i+=2

#4)find the sum of 100 numbers
sum=0
for i in range(101):
   sum+=i  
print(sum)

i=0
sum=0
while i<=100:
   sum+=i
   i+=1
print("Sum of 100 numbers from 1 to 100",sum)

# 5)program to print product of 10 numbers
mul=1
for i in range(1,10):
   mul*=i
   i+=1
print(mul)   

# 6)print multipilcation table of any number
n=int(input("enter a number:"))
for i in range(11):
   print(f"{n} * {i} = {n*i}")
   





# 7) program to count digits in number
a=str(3423535)
digits=0
for i in a:
   digits+=1
print(digits)


b=143
res=0
while b>0:
   rem=b%10
   res+=1
   b=b//10
print(res)   
      

# 8)calculate the sum of digits of a number
s=654
sum=0
while s>0:
    rem=s%10
    sum+=rem
    s=s//10
print(sum)  

# 9)reverse of given number using a loop
s=654
num=0
while s>0:
    digit=s%10
    num=num*10+digit
    s=s//10
print("Reverse of  number is",num)  


#print numbers from 1 to 100 that are divisible by 3 and 5
for i  in range(1,101):
    if i%3==0 and i%5==0:
        print(i)

# factorial of number using for loop
n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
        fact=fact*i            
print(fact)        


n=int(input("enter a number:"))
fact=1
while n>0:
     fact*=i
     i+=1
print(fact)     

#program to find fibonacci
n=int(input("enter nterms to be generate:"))
a=0
b=1
print(a,b,end=" ")
for i in range(n):
    c=a+b
    print(c,end=" ")
    a,b=b,c

#count odd and 
a=45678482
even_count=0
odd_count=0
num=0
while a>0:
    num=a%10 
    a=a//10 
    if num%2==0:
        even_count+=1       
    else:
        odd_count+=1       
print("count of odd digits",odd_count)    
print("count of even digits",even_count)    
  
#find largest digit in a number
a=65374858
rem=0
max=0
while a>0:
    rem=a%10
    a=a//10
    if rem>max:
        max=rem
print(max)

#program to find smallest digit in number
a=65374858
rem=0
max=float('inf')
while a>0:
    rem=a%10
    a=a//10
    if rem<max:
        max=rem
print(max)

#program to find power of a number without using the ** operator
n=int(input("enter a number:"))
power=5
res=1
for i in range(power):
    res*=n
print(res)  

#program to find palindrome or not
n=121
i=n
temp=0
while n>0:
    rem=n%10 
    temp=temp*10+rem
    n=n//10
if (i==temp):
    print("palindrome",temp)
else:
    print("not plaindrome")    

# strings
s="Hey"
print(s.replace('H','Z'))
z=" yedh "
print(z.strip())
print(s[-1])

#print character in a string
s="hello"
for i in s:
    print(i)

#count vowels and consonants
v_count=0
c_count=0
s="pragati"
for i in s:
    if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
        v_count+=1
        
    else:
        c_count+=1
print("vowels count",v_count)
print("consonant count",c_count)     

s="pragti"
if "i"  in s:
    print("hello")

#reverse a string using loop
s=input("enter a string:")
res=""
for i in s:
    res=i+res
print(res)  

for i in range(len(s)-1,-1,-1):
    print(s[i])

#ascii values
print(ord('a'))

#count uppercase and lower case
s="FFSfs"
u_count=0
l_count=0
for i in s:
    if i.isupper():
        u_count+=1
    else:
        l_count+=1
print(u_count)
print(l_count)

a="Hf"
up_count=0
lo_count=0
for char in a:
    ascii=ord(char)
    if ascii>=97 and ascii<=122:

      lo_count+=1
    elif ascii>=65 and ascii<=80:
      up_count+=1    

print(up_count)
print(lo_count)

#reverse palindrome
s="deel"
res=""
for i in s:
    res=i+res
print(res)  
if s==res:
   print("palindrome")
else:
    print("not plaindrome")

for i in range(len(s)-1,-1,-1):
    print(s[i])

#program to print vowels in a string
s="pragati"
for i in s:
    if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
        print(i)
        

#find the number of spaces,digits and special characters
s="345 $"
s_count=0
digi_count=0

sp_count=0
for char in s:
    if char==" ":
        s_count+=1
    elif 48<=ord(char)<=57:
        digi_count+=1
    elif 32<=ord(char)<=47:
        sp_count+=1
print(digi_count,s_count,sp_count)           

s="pragati"
for i in s:
    if i not in "aeiouAEIOU":
        print(i)
#every seconf char
S="GAEGRQE"
for i in range(2,len(S),2):
    print(S[i])

# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("inverse triangle")
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(5):
    for j in range(5-i):
        print("*",end=" ")
    print()

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *

print("pyramid")
for i in range(6):
    for j in range(6-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")    
    print()    

