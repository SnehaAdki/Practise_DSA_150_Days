# Valid Anagram

# https://leetcode.com/problems/valid-anagram/submissions/1841119236/

# 242. Valid Anagram
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_s = {}
        hash_t = {}
        
        for i in range(0,len(s)):
            hash_s[s[i]] = hash_s.get(s[i],0)+1
            hash_t[t[i]] = hash_t.get(t[i],0)+1
            
        for counter in hash_s:
            if hash_s[counter] != hash_t.get(counter,0):
                return False
        return True