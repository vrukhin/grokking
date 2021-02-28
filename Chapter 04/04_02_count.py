#!/usr/bin/python

def count(nums):
    if nums == []:
        return 0
    else:
        return 1 + count(nums[1:])
        
print(count([2,4,6]))
