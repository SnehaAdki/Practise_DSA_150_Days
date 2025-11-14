# Intersection of Two Arrays II

# https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/1829510163/

# 350. Intersection of Two Arrays II
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two integer arrays nums1 and nums2, 
# return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

def get_all_common(num1,num2):
    if len(num2) < len(num1):
        num1,num2 = num2 ,num1
        
    common_ele = []
    for i in range(0,len(num1)):
        if num1[i] in num2:
            num2.remove(num1[i])
            common_ele.append(num1[i])

    print(common_ele)
    
    
num2 = [1,2]
num1 = [2,1]
get_all_common(num1, num2)