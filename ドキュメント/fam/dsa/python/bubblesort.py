def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]<list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
list=[10,50,40,20,70]
bubblesort(list)            
    