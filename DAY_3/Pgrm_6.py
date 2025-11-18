# Valid Mountain Array
# The link `https://leetcode.com/problems/valid-mountain-array/submissions/1833350191/` is a URL to a
# specific problem on the LeetCode platform. It seems to be related to the problem of determining
# whether a given array is a valid mountain array based on certain conditions. The code provided below
# the link is a Python function `validate_mountain` that attempts to solve this problem by checking if
# the array meets the criteria of a mountain array. The function iterates through the array to find
# the first peak and then validates if the elements before and after the peak satisfy the mountain
# array conditions.
# https://leetcode.com/problems/valid-mountain-array/submissions/1833350191/

# 941. Valid Mountain Array
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
 

# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true

def validate_mountain(arr_val):
    first_peak = None
    for i in range(1,len(arr_val)-1):
        if arr_val[i]>arr_val[i-1] and arr_val[i]>arr_val[i+1]:
            first_peak = i
            break
    
    #if no peak
    if first_peak == None :
        return False
    
    for i in range(0,first_peak):
        if not arr_val[i] < arr_val[i+1]:
            return False
        
    for i in range(first_peak,len(arr_val)-1):
        if not arr_val[i] > arr_val[i+1]:
            return False

    return True
arr_val = [2,1]
print(validate_mountain(arr_val))
