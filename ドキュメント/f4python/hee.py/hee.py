string =input("enter a string:")
p = ""
for i in string:
    if i not in p:
        p = p+i
print(p)
