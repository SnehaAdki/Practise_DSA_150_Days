# # Is Subsequence

# # https://leetcode.com/problems/is-subsequence/submissions/1841691696/

# 392. Is Subsequence
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if len(s)==0:
            return True
        achieved = []
        j=0
        for i in range(0,len(t)):
            if s[j] == t[i]:
                achieved.append(s[j])
                if j<len(s)-1:
                    j+=1
                else:
                    break
                
            
        return ''.join(achieved) == s
