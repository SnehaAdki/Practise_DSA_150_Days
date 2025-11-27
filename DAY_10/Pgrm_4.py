# Longest Common Prefix

# https://leetcode.com/problems/longest-common-prefix/submissions/1841111918/

# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        def get_common(fst,sec):
            i =0 
            while i < len(fst):
                if fst[i]!=sec[i]:
                    break
                i+=1
            return fst[:i]

        strs.sort(key=len)
        output = ''
        first = strs[0]
        for j in range(1,len(strs)):
            if len(strs[j]) >= len(first) or len(strs[j])> output:
                output = get_common(first,strs[j])
                print("------")
                print(first)
                print(strs[j])
                print(output)
                first = output
        return output