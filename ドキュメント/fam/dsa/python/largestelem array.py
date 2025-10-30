def largest_of_array(arr):
    if not array:
        return "Array is not empty"
    else:
        largest=arr[0]
        for ele in arr:
            if ele>largest:
                largest=ele
        return largest
array=[6,78,5,104,67,89,789999]  
print(largest_of_array(array))          
