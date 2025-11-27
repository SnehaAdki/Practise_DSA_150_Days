# Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/submissions/1841102697/

# 409. Longest Palindrome
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.
 

# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_map = {}
        old_count = 0
        for i in s:
            if hash_map.get(i):
                hash_map[i] += 1
            else:
                hash_map[i] =1
                
            if hash_map[i]%2 ==1 :
                old_count += 1
            else:
                old_count -= 1
        if old_count >1:
            return len(s)-old_count+1
        return len(s)
                