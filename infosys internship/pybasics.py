name="anusha"
fav_language="python"
year="2025"
has_coded_before=True
print(name)
print(fav_language)
print(year)


city_list=["chennai","mumbai","delhi","jaipur","punjab"]
print("First City:",city_list[0])
city_list.append("kerala")
print(city_list)
city_list.pop(2)
print(city_list)


tuple=("anusha","658544345")
print("name:",tuple[0])
print("number:",tuple[1])


dict={"name":"anusha","age":20,"fav_lang":"c"}
print(dict["fav_lang"])
dict["fav_lang"]="python"
print(dict)

#day 2

for num in range(1001,1006):
    print(f"MH01AB{num}")

speeds=[72,85,60,95,78]
for a in speeds:
    if a>80:
        print("violations",a)

speeds=[72,85,60,95,78]
count=0
for a in speeds:
    if a>80:
        count+=1
print("number of violations:",count)   

#print vehice &speed

plates=['MH12AB1234','MH14CD5678','MH12EF9012']
speeds=[65,95,85]
for s,p in zip(speeds,plates):
    print(s,p)

#home work

records=[
    ('MH12AB1234',75,'Car'),
    ('MH14CD5678',92,'Truck'),
    ('MH12EF9012',60,'Bike'),
    ('MH14XY3344',102,'Car'),
    ('MH19GH7788',78,'SUV'),
    ('MH20KL1122',88,'Truck')
]

#print all vehicle plate numbers
print("vehicle plate numbers:")
for rec in records:
    print(rec[0])

#print all vehicle speeds 
print("vehicle speed:")
for reco in records:
    print(reco[1])

#count
count=0
for rec in records:
    count+=1
print("numbers vehicle plates:",count)

#plate number
result=[rec[0] for rec in records]
print("list of number plates:",result)    


#print every second vehicle in the log

for i in range(1,len(records),2):
    print(records[i])    



colour=input("enter a traffic colour(red/green/yellow):")
condition=input("enter a condition(moving/not moving):")
if colour=="red" and condition=="moving":
    print("violation detected")
elif colour in ["red","yellow","green"]:
    print("traffic light in",colour,"colour")
else:
    print("please enter a valid traffic colour")        


#lambda 
add=lambda x,y:x+y
print(add(3,5))