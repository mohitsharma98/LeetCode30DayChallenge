"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.
"""

class Solution:
    def moveZeroes(self, nums) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[count] = nums[i]
                count+=1
        while count<len(nums):
            nums[count] = 0
            count+=1