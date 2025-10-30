
#list (it stores multiple data types,it is ordered,it is changeable,it allows duplicates,dynmaic)
a=[1,2,4]
print(type(a))
a=[1,"ge",2.54,6+8j]
print(type (a))

#list methods (append,pop(it removes last ele),insert(at specified position),remove(specified elem),extend(it add more elements to alist))
d=[3,5,6,7]
print(d)
d.append(8)
print(d)
d.pop()
d.pop(2)
d.insert(1,50)
d.remove(50)
print(d)
g=[10,20,30]
h=[40,50,60]
c=g+h 
# "+" concatenates two strings
print(c)
#sorting of array 
#diff between .sort() and sorted(it stores in another list
a=[45,76,24,85]
b=sorted(a)
print(b)
c=sorted(a,reverse=True)#reverse of list
print(c)
h=[6,65,78,-1,100,5]
h[1]=108
print(h)
for ele in h:
    print(ele)

#slicing
a=[5,76,3,-1,54]
print(a[1:4])
print(a[::4])
a[1:4]=[78]
print(a)

a=[3,4]*5
b=[6]*9
print(b)
print(a)

a=[[3,4,5],[7,8,9]]
print(a)
b=list(a)
print(b)
a.append([89,65])
print(a)
a[0][1]=100
print(a)

#Tuple (it is ordered ,it is unchangeable,it allows duplicates)
a=(2,3,5)
print(type(a))
print(list(a))
a=([1,2,3],[3,5,6])
print(a)

#set (unordered,unchangeable,unindexed)
a={1,23,54}
print(type(a))
a.add(4)
print(a)

#dictionary (ordered,changable,no dupliactes allow)
a={"name":"dep","id":12}
print(a["name"])
a["name"]="hii"
del a["id"]
print(a)
for k,v in a.items():
    print(a)
a.update({"id":89})
print(a)
a.clear()
print(a)

#create list of 5 numbers and sum them
list=[1,2,3,4,5]
sum=0
for i in list:
    sum+=i
print(sum)    

#finf the largest ans smmalest number in a list
a=[1,2,56,78]
smallest=float('inf')
largest=float('inf')
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
    elif a[i]<smallest:
        smallest=a[i]
print("large num in list:",largest)
print("large num in list:",smallest)           

#reverse of list
a=[1,2,3,4]
print(a[::-1])
d=[45,65,867]
res=[]
for i in range(2,0,-1):
    res.append(d[i])
print(res)

f=[5,7645,3534]
rev=[]
for i in f:
    rev.insert(0,i)
print(rev)    

#remove dupliactes in a list
a=[3,4,3,5]
res=[]
for i in a:
    if i not in res:
        res.append(i)
print(res)        

#count how many items each ele appears in a list

b=[3,4,4,5,6,7,7]
a={}
for i in b:
    if i  in a:
        a[i]+=1
    else:
        a[i]=1
print(a.items())                
     
    #second largest in a list
s=[4,5,6,7]
largest_num=a[0]
second_largest=largest_num
for ele in s:
    if ele>largest_num:
        second_largest=largest_num
        largest_num=ele
    elif ele>second_largest and ele<largest_num:
        second_largest=ele
           

    
#functions
def add(a,b):
    c=a+b
    return c
print(add(2,3))

#program to print division of number using fun
def div(a,b):
    c=a/b
    print(c)
div(6,2)    

x=lambda a:a*10
print(x(5))
#fibonacci using fun
def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(8))
    
#merge two lists and remove duplicates
a=[1,2,3,4]
b=[5,6,5,6,7,7,8]
c=a+b
print(c)
res=[]
for i in c:
    if i not in res:
        res.append(i)
print(res)        

def merge(s,h):
    c=s+h
    return c
    res=[]
    for i in c:
        if i not in res:
            res.append(i)
        print(res)        
print(merge([1,2],[3,4]))


#palindrome of list using func

def palin(s):
    res=[]
    for i in s:
        res.insert(0,i)
    if res==s:
        return "palindrome"
    else:
        return "not palindrome"
s=[1,2,1]
print(palin(s))        

#find common ele between two list
a=[1,2,4,5]
b=[2,4,6]
res=[]
for i in a:
    if i in b:
        res.append(i)
print(res)        

def common(l1,l2):
    res=[]
    for i in l1:
        if  i in l2:
            res.append(i)
    return res
print(common([1,2,3,9],[2,4,1,9]))        
   

#square of every of number in a list using loop
def square(s):
 res=[]
 for i in s:
    res.append(i*i)
 return res
s=[1,2,3,4]
print(square(s))

#get even and odd numbers seperately
def even_odd(s):
  even=[]
  odd=[]
  for i in s:
    if i%2==0:
      even.append(i)
    else:
      odd.append(i) 
  return even,odd
  
  
print(even_odd([1,2,3]))   

# replace all negative numbers with zero
def list(s):
  res=[]
  for i in s:
    if i<0:
      i=0
    res.append(i)
  return res
print(list([1,2,3]))

      
#rotate a list by k elements to the right
s=[1,2,3,4,5]
k=int(input("enter: "))
def rotate(s,k):
  k=k%5
  t=len(s)-k 
  return s[t:]+s[:t]
print(rotate(s,k))

#sorting of lsit without using sort function

#tuple and each element
s=(1,2,4,"hii")
for i in s:
  print(i)

#find the length of tuple without using len()
s=(1,2,3,4)
def length(s):
  count=0
  for i in s:
    count+=1
  return count
print(length(s))  

#convert list into a tuple and tuple 
s=[1,2,3]
print(tuple(s))

#concatenate 2 tuples and print the result
s=(1,2,3)
d=(3,4,5)
print(s+d)

#find max and min value in tuple
def maxi_mini(s):
  maxi=0
  mini=float('inf')
  for i in s:
    if i>maxi:
      maxi=i
    elif i<mini:
      mini=i
  return maxi,mini
print(maxi_mini((1,2,4,9,3)))    

target =6
def check(s,target):
  for i in s:
    if sum(i)==target:
      return True
  return False
print(check((1,2,3),6))