
# Binary Tree Postorder Traversal

# https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/1836009318/

# 145. Binary Tree Postorder Traversal
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [3,2,1]


# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,6,7,5,2,9,8,3,1]


# Example 3:
# Input: root = []
# Output: []

# Example 4:
# Input: root = [1]
# Output: [1]


# Definition for a binary tree node.

from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def post_order(self,temp,final_arr):
        if temp == None:
            return None
        self.post_order(temp.left,final_arr)
        self.post_order(temp.right,final_arr)
        final_arr.append(temp.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        final_arr = []
        temp = root
        self.post_order(temp,final_arr)
        return final_arr