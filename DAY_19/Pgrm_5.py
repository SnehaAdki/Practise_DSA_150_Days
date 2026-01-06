# Kth Missing Positive Number
# https://leetcode.com/problems/kth-missing-positive-number/submissions/1876618957/
# 1539. Kth Missing Positive Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

# Return the kth positive integer that is missing from this array.


# Example 1:
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

# Example 2:
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        maxim = max(arr)
        for i in range(1,maxim+1):
            if i not in arr:
                count = count + 1
            if count == k:
                return i
        if k!=count:
            return maxim+(k-count)
        


print(Solution().findKthPositive(arr = [1,2,3,4], k = 2))
