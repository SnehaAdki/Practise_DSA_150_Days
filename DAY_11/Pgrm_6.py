# Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/submissions/1841712009/

# 1047. Remove All Adjacent Duplicates In String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

# We repeatedly make duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.


# Example 1:
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

# Example 2:
# Input: s = "azxxzy"
# Output: "ay"

class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s)<0:
            return s
        stack_val = [s[0]]
        for i in range(1,len(s)):
            if len(stack_val) > 0 and stack_val[-1] == s[i]:
                stack_val.pop()
            else:
                stack_val.append(s[i])

        return ''.join(stack_val)