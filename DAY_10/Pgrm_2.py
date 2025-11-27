# Valid Palindrome II

# https://leetcode.com/problems/valid-palindrome-ii/submissions/1841085735/

# 680. Valid Palindrome II
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def get_pal(l,r):
            while l <r:
                if s[l] !=s[r]:
                    return False
                l+=1
                r-=1
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left+=1
                right-=1
            else:
                return get_pal(left+1 , right) or get_pal(left,right-1)
        return True