#!/usr/bin/python

def quickSort(nums):
    if len(nums) < 2:
        return nums
        
    pivot = nums[0] # опорный элемент
    less = [i for i in nums[1:] if i <= pivot]
    greater = [i for i in nums[:] if i > pivot]
    
    return quickSort(less) + [pivot] + quickSort(greater)
    
print(quickSort([10, 5, 2, 3]))
