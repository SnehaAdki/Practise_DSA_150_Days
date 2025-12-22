# Hamming Distance
# https://leetcode.com/problems/hamming-distance/submissions/1862525574/
# 461. Hamming Distance
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.



# Example 1:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

# Example 2:
# Input: x = 3, y = 1
# Output: 1


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = 0

        bin_x = bin(x).replace("0b","")
        bin_y = bin(y).replace("0b","")

        if len(bin_x)>len(bin_y):
            bin_y = '0'*(len(bin_x)-len(bin_y)) + bin_y
        else:
            bin_x = '0'*(len(bin_y)-len(bin_x)) + bin_x

        for i in range(0,len(bin_y)):
            if bin_x[i] != bin_y[i]:
                diff = diff +1
        return diff