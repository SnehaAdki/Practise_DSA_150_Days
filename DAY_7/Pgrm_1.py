# Binary Tree Preorder Traversal
# https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1836003995/

# 144. Binary Tree Preorder Traversal
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return the preorder traversal of its nodes' values.



# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [1,2,4,5,6,7,3,8,9]
# Explanation:


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

    def pre_order(self,temp,final_arr):
        if temp == None: 
            return None
        final_arr.append(temp.val)
        self.pre_order(temp.left,final_arr)
        self.pre_order(temp.right,final_arr)
        


    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        temp = root
        final_arr= []
        self.pre_order(temp,final_arr)
        return (final_arr)