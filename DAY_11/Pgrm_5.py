# Isomorphic Strings

# https://leetcode.com/problems/isomorphic-strings/submissions/1841706996/

# The code you provided is a Python solution to the LeetCode problem "Isomorphic Strings". The problem
# asks you to determine if two given strings, `s` and `t`, are isomorphic. Two strings are considered
# isomorphic if the characters in `s` can be replaced to get `t`, following certain rules.

# 205. Isomorphic Strings
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.


# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Explanation:
# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true




class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        for i in range(0,len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = i

            if t[i] not in dict_t:
                dict_t[t[i]] = i

            if dict_t[t[i]] != dict_s[s[i]]:
                return False
        return True