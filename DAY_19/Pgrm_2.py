# Search Insert Position

# https://leetcode.com/problems/search-insert-position/submissions/1876547479/?page=1&search=j%3D0+++++for+i+in+range%28len%28nums%29%29%3A+++++++++if+nums%5Bi%5D+%21%3D+0%3A+++++++++++++nums%5Bj%5D+%3D+nums%5Bi%5D+++++++++++++j%2B%3D1+++++while+j+%3C+len%28nums%29%3A+++++++++nums%5Bj%5D%3D0+++++++++j%2B%3D1+++++return+nums
# Code
# Testcase
# Test Result
# Test Result
# 35. Search Insert Position
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.



# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            # elif nums[i] == target:
            #     return i
            i+=1
        return len(nums)
        
print(Solution().searchInsert([1,3,5,6],5))
print(Solution().searchInsert([1,3,5,6],2))
print(Solution().searchInsert([1,3,5,6],7))