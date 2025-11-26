# Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/submissions/1840322250/

# 110. Balanced Binary Tree
# Easy
# Topics
# premium lock icon
# Companies
# Given a binary tree, determine if it is height-balanced.


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true


# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root == None:
                return 0
            lh = check(root.left)
            rh = check(root.right)
            
            if lh == -1 or rh == -1:
                return -1
            
            if (lh - rh) > 1 or (rh - lh) > 1:
                return -1
                
            return max(lh,rh)+1
        return True if check(root) >=0 else False

