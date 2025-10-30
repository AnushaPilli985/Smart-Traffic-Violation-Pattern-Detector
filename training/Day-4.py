'''
def add(a,b=8):
   c=a+b
   return c
print(add(3,5))

def add(*d):#args take any number of arguments while calling function 
   return d
print(add(3,5,6))
   
def collect(**f):#kwargs it takes arguments in key values
   return f
print(collect(name="hii",age=78))

#oops#

class Details:
   def __init__(self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender
    
   def display(self):
    print(self.name)
    print("showing and acting")
   def job(self):
    print("acting")

d=Details("hii",67,"male")
print(d.name,d.age,d.gender)
d.display()
d.job()

class Food:
  def __init__(self,name,taste,colour):
    self.name=name
    self.taste=taste
    self.colour=colour
  def non_veg():
    print("very tasty")
  def veg():
    print("tasty")   

f=Food("chicken","red","super")
print(f.name,"is ",f.taste," in colour"," and taste is",f.colour)

class student:
  def __init__(self,name,branch,section,rollno):
    self.name=name
    self.branch=branch
    self.section=section
    self.rollno=rollno
  def display(self):
    return self.name,self.branch,self.section,self.rollno
s=student("rani","cse","c",56)
s1=s.display()
print(s1) 

class mobile:
  def __init__(self,company,colour,cost):
    self.company=company
    self.colour=colour
    self.cost=cost
  def show(self):
    print(f"{self.company} mobile ,colour is {self.colour} ,cost is {self.cost}")
m=mobile("iphone","white","70k")
m1=m.show()

class Bank:
  def __init__(self):
    self.name="ram"
    self.amount=3000
    self.__password="1234"#private variable
  def setter(self,new_password):
    self.__password=new_password
  def getter(self):
    return self.__password

b=Bank()
print(b.name)
b.setter("43534")
print(b.getter())

class email:
  def __init__(self):
    self.name="rama"
    self.__password="425a"
  def set_psw(self,new_password):
    self.__password=new_password
  def get_psw(self):
    return self.__password
e=email()
e.set_psw("457d")
print(e.get_psw())

# 1 1 1 1 1  
# 2 2 2 2 2  
# 3 3 3 3 3  
# 4 4 4 4 4  
for i in range(1,5):
  for j in range(5):
    print(i,end=" ")
  print(" ")

# 1
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(1,6):
  for j in range(1,i):
    print(j,end=" ")
  print(" ")

# 1
# 2 3
# 4 5 6
# 7 8 9 10
n=1
for i in range(1,5):
  for j in range(i):
    print(n,end=" ")
    n+=1
  print(" ")  

print("ygvyt")
n=10
for i in range(n):
  for j in range(n-i):
    print(n,end=" ")
    n-=1
  print(" ")  


# for i in range(5):
#   for j in range(i):
#     print(char(65))

# A
# B B
# C C C
# D D D D
# E E E E E
a=65
for i in range(5):
  for j in range(i+1):
    print(chr(a),end=" ")
  a+=1
  print()  

for i in range(5):
  for j in range(5):
    if i==0 or  j==5-1 or  j==0 or i==5-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")  
  print( )    

#count totall no of factors of a number

count=0
num=20
for i in range(1,20+1):
  if 20%i==0:
    count+=1
  
print(count)    


#prime number

# count=0
# def prime(n):
#   for i in range(n+1):
#     if n%i==0:
#       count+=1
#   if count==2:
#     return n
# n=47
# if prime(n):
#   print("prime")

count=0
def prime(n):
  for i in range(2,n//2):
    if n%i==0:
      return False
    return True
n=48
print(prime(n))

n=100
count=0
for i in range(1,100):
  if n%i==0:
    count+=1
i+=1
if count<=2:
  print("prime number",n)
else:
  print("not number")
'''
#amstrong number
num=154
res=0
temp=num
length=len(str(num))
while num>0:
  last=num%10
  res+=(last**length)
  num=num//10
if res==temp:
  print("amstrong")
else:
  print("it is not an amstrong")