# Binary Tree Inorder Traversal

# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/1836006724/
# 94. Binary Tree Inorder Traversal
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]



# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [4,2,6,5,7,1,3,9,8]



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
    def inorder(self,temp,final_arr):
        if temp == None:
            return None
        self.inorder(temp.left,final_arr)
        final_arr.append(temp.val)
        self.inorder(temp.right,final_arr)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        final_arr =[]
        temp = root
        self.inorder(temp,final_arr)
        return final_arr
