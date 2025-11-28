# Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/submissions/1841728511/

# 917. Reverse Only Letters
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.


# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"

# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"

# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        str_list = list(s)
        i =0 
        j = len(str_list)-1

        while i < j:
            if str_list[i].isalpha() and str_list[j].isalpha():
                str_list[i] , str_list[j] = str_list[j],str_list[i]
                i+=1
                j-=1
            elif str_list[i].isalpha() and not str_list[j].isalpha():
                j-=1
            elif not str_list[i].isalpha()  and  str_list[j].isalpha():
                i+=1
            else:
                i+=1
                j-=1

        
        print(str_list)
        return  ''.join(str_list)