#!/usr/bin/python

def total(nums):
    if nums == []:
        return 0
    else:
        return nums.pop(0) + total(nums)
        
print(total([2,4,6]))

