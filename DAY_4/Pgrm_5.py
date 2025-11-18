# Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/submissions/1833469606/

# 485. Max Consecutive Ones
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:
# Input: nums = [1,1,0,1,1,1]


# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2


def max_ones(arr):
    final = 0
    count = 0
    for i in range(0,len(arr)):
        if arr[i] != 0:
            count = count+1
        elif arr[i] == 0:
            final = max(count,final)
            count = 0

    print(max(count,final))


nums = [1,1,0,1,1,1]
max_ones(nums) 