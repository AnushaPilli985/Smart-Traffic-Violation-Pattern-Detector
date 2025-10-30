def mergeSort(nums):
        if i<len(nums):
            return nums
        mid=len(nums)//2
        left=mergeSort(nums[:mid])
        right=mergeSort(nums[mid:])

        sorted_list=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
               sorted_list.append(left[i])
               i+=1
            else:
               sorted_list.append(right[j])
               j+=1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])  
        return sorted_list

 
my_list=[5,3,6,9,2]
print(mergeSort(my_list))
