#!/usr/bin/python

def maximum(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        return max(nums.pop(), maximum(nums))
        
        
print(maximum([2,4,6]))


def maximum2(nums):
    if len(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]
    sub_max = maximum2(nums[1:])
    return nums[0] if nums[0] > sub_max else sub_max
        
print(maximum2([2,4,6]))
