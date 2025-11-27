# First Unique Character in a String

# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/1841126744/


# 387. First Unique Character in a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation:
# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

class Solution:
    def firstUniqChar(self, sub_arr: str) -> int:
        i = 0 
        for i in range(0,len(sub_arr)):
            if i==0:
                sub = sub_arr[i+1:]
            else:
                sub = sub_arr[0:i]+sub_arr[i+1:]
            if sub_arr[i] not in sub:
                return i
        return -1