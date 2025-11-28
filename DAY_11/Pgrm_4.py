# Reverse Words in a String III

# https://leetcode.com/problems/reverse-words-in-a-string/submissions/1841703637/

# 151. Reverse Words in a String
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


class Solution:
    def reverseWords(self, s: str) -> str:
        str_arr = s.split(' ')
        while '' in str_arr:
            str_arr.remove('')
        i = 0
        j = len(str_arr)-1
        while i < j:
            str_arr[i] ,str_arr[j] = str_arr[j],str_arr[i]
            i+=1
            j-=1
        
        return ' '.join(str_arr)