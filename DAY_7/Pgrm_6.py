# Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/submissions/1836041688/
# 101. Symmetric Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



# Example 1:
# # Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false


# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sym_verify(self,left,right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        return left.val == right.val and self.sym_verify(left.left,right.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return None
        return self.sym_verify(root.left,root.right)

