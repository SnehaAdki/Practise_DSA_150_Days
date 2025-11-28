# Reverse String
# https://leetcode.com/problems/reverse-string/submissions/1841693308/

# 344. Reverse String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.



# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]



from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i < j:
            s[i] ,s[j] = s[j],s[i]
            i+=1
            j-=1
        
        print(s)