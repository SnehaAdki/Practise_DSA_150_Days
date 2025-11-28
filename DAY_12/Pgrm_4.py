# Length of Last Word
# https://leetcode.com/problems/length-of-last-word/submissions/1841732944/

# 58. Length of Last Word
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_list = s.split(" ")
        arr = []
        print(str_list)
        for i in range(0,len(str_list)):
            if str_list[i] !='':
                arr.append(str_list[i])

        return len(arr[-1])