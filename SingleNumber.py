""" 
Given a non-empty array of integers, every element appears twice except for one. Find that single one. 
Input: [4,1,2,1,2]
Output: 4
"""

class Solution:
    def singleNumber(self, nums) -> int:
        a = nums[0]
        for i in range(1, len(nums)):
            a = a ^ nums[i]
        return a