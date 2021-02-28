#!/usr/bin/python

def maximum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums.pop(), maximum(nums))
        
print(maximum([2,4,6]))
