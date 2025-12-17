# Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-numbers/submissions/1858144619/ 

# 628. Maximum Product of Three Numbers
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.



# Example 1:
# Input: nums = [1,2,3]
# Output: 6

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 24

# Example 3:
# Input: nums = [-1,-2,-3]
# Output: -6



from typing import List
from functools import reduce

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
        
        
        
print(Solution().maximumProduct([-100,-98,-1,2,3,4]))
# print(Solution().maximumProduct([-1,-2,-3]))
