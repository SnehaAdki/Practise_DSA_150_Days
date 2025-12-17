# Add Digits
# https://leetcode.com/problems/add-digits/submissions/1858128860/
# 258. Add Digits
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0


from functools import * 
class Solution:
    def addDigits(self, num: int) -> int:
        val = reduce(lambda a,b: int(a)+int(b) , list(str(num)))
        print(val)
        if int(val) < 10:
            return int(val)
        return self.addDigits(val)
    
print(Solution().addDigits(0))
