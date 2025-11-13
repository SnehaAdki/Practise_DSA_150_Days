# 4: Move Zeroes
# https://leetcode.com/problems/move-zeroes/submissions/1828998140/
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

def move_zeros(nums):
    j=0
    for i in range(0,len(nums)):
        if nums[i] !=0:
            nums[j] = nums[i]
            j+=1
    while j < len(nums):
        nums[j] = 0
        j+=1
print(move_zeros(nums=[1,1,0,3,12]))