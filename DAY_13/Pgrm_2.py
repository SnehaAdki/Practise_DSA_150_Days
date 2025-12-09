# Palindrome Number
# https://leetcode.com/problems/palindrome-number/submissions/1851241685/

# 9. Palindrome Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer x, return true if x is a palindrome, and false otherwise.



# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution:
    def isPalindrome(self, x) -> bool:
        if x < 0 :
            return False
        abc = x
        val = ''
        while x != 0:
            rem  = (x%10)
            x = x // 10
            val = val + str(rem)
        print(val)
        return abc == int(val)
        
val = -121
print(Solution().isPalindrome(0))
# Solution.isPalindrome(val)