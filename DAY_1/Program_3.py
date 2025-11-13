#3: Majority Element
# https://leetcode.com/problems/majority-element/submissions/1828983202/
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def return_majority(ele):
    hash_map = {}
    for i in range(0,len(ele)):
        if hash_map.get(ele[i]):
            hash_map[ele[i]]+=1
        else:
            hash_map[ele[i]] =1
        if hash_map[ele[i]] > (len(ele)//2):
            return ele[i]

nums = [1]
print(return_majority(nums))
