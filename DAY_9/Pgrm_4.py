# Convert Sorted Array to Binary Search Tree

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/1841031844/

# 108. Convert Sorted Array to Binary Search Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(l,r):
            if l > r:
                return None
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left = bst(l,m-1)
            root.right = bst(m+1,r)
            return root
        
        return bst(0,len(nums)-1)