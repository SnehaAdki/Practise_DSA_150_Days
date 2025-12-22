# Add Binary
# https://leetcode.com/problems/add-binary/submissions/1859130287/
# 67. Add Binary
# Easy
# Topics
# premium lock icon
# Companies
# Given two binary strings a and b, return their sum as a binary string.


# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, d1: str, d2: str) -> str:
        sum = ""
        carry = 0
        d1,d2 = d1[::-1],d2[::-1]
        for i in range(max(len(d1),len(d2))):
            digitA = ord(d1[i]) - ord("0") if i < len(d1) else 0
            digitB = ord(d2[i]) - ord("0") if i < len(d2) else 0
        
            total = digitA + digitB + carry        
            carry = total %2
            sum =sum + str(carry)
            carry = total // 2
        sum =sum + str(carry) if carry else sum
        return sum[::-1]
    
    

a = "01"
b = "1"    
Solution().addBinary(a,b)