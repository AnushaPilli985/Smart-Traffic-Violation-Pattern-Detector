#lambda 
add=lambda x,y:x+y
print(add(3,5))
def add(x,y):
    return x+y
print(add(7,6))

#use of lambda with filter
records=[80,130,100,60,50,70,120]
limit=80
violation=list(filter(lambda x:x-limit>20,records))
print("driver speed exceeded the speed limit by more than 20 km/h:",violation)

#17-09-2025 task
records=[80,130,100,60,50,70,120]
limit=80
base_fine=1000
fines=list(map(lambda x:(x,2.0 if x>limit+30 else (1.5 if x> limit+15 else 1.0),),records))
violations=[(speed,multiplier,base_fine*multiplier)
            for speed,multiplier in fines if speed>limit]

print("violations and fines:")
for speed,multiplier,fine in violations:
    print(f"speed:{speed}km/h | Multiplier:{multiplier}|Fine:{fine}")