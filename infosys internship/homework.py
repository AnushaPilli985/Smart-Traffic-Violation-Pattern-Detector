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

#12-09-25 assignment

print("**violation checking**")

def check_violations(speed,road_type,safety_gear,vehicle_number,date):
    if road_type=="Highway":
        limit=100
    elif road_type=="City":
        limit=60
    elif road_type=="School Zone":
        limit=30 
    else:
        return "Invalid road type"

    violations=[]    

    #speed check   
    if speed>limit:
        violations.append("Speed Violation")

     #safety gear check   
    if not safety_gear:
        violations.append("Speed gear violation")

    #odd even rule check
    last_digit=int(vehicle_number[-1])
    if (date%2==0 and last_digit%2!=0) or(date%2!=0 and last_digit%2==0):
        violations.append("odd-even rule violation")

    if violations:
        return "Violations:" + ",".join(violations)  
    else:
        "No violations" 

print(check_violations(60,"City",False,"MBH1234",4))

#17 9 home work(2)

# Speeds recorded
records = [80, 130, 100, 60, 50, 70, 120]
limit = 80
base_fine = 1000  # ₹1000

print("Violations and fines:")

# Go through each driver's speed
for speed in records:
    if speed > limit:   # only check violators
        # Find how much over the limit
        extra = speed - limit

        # Decide multiplier
        if extra > 30:
            multiplier = 2.0
        elif extra > 15:
            multiplier = 1.5
        else:
            multiplier = 1.0

        # Final fine = base fine × multiplier
        fine = base_fine * multiplier

        # Show result
        print(f"Speed: {speed} km/h | Multiplier: {multiplier} | Fine: ₹{fine}")








