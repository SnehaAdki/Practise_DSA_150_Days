# 5: Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/submissions/1829000306/

# 977. Squares of a Sorted Array
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def return_sorted(nums):
    for i in range(0,len(nums)):
        nums[i] = nums[i] * nums[i]
    nums.sort()
    return nums


print(return_sorted([-4,-1,0,3,10]))

