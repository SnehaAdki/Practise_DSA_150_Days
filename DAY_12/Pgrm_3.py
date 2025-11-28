# Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1841730128/

# 345. Reverse Vowels of a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        str_list = list(s)
        i =0 
        j = len(str_list)-1

        while i < j:
            if str_list[i].lower() in ('a','e','i','o','u') and str_list[j].lower() in ('a','e','i','o','u'):
                str_list[i] , str_list[j] = str_list[j],str_list[i]
                i+=1
                j-=1
            elif str_list[i].lower() in ('a','e','i','o','u') and not str_list[j].lower() in ('a','e','i','o','u'):
                j-=1
            elif not str_list[i].lower() in ('a','e','i','o','u') and  str_list[j].lower() in ('a','e','i','o','u'):
                i+=1
            else:
                i+=1
                j-=1

        
        print(str_list)
        return  ''.join(str_list)