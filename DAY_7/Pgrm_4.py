# Maximum Depth of Binary Tree

# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/1836015410/


# 104. Maximum Depth of Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2




# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def get_max_depth(self,temp):
        if temp == None:
            return 0
        return 1 + max(self.maxDepth(temp.left) , self.maxDepth(temp.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_max_depth(root)