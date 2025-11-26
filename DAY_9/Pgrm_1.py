# Path Sum

# https://leetcode.com/problems/path-sum/submissions/1840353708/

# 112. Path Sum
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.


# Example 1:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There are two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        
        sum_path = [] #holds the path value
        sum_node = [] # in sync with that node
        
        sum_path.append(root.val)
        sum_node.append(root)
        
        while (len(sum_node) !=0):
            temp_node = sum_node.pop()
            temp_val = sum_path.pop()
            
            if temp_node.right == None and temp_node.left == None and temp_val == targetSum:
                return True
            
            if temp_node.right:
                sum_node.append(temp_node.right)
                sum_path.append(temp_node.right.val+temp_val)
                
            if temp_node.left:
                sum_node.append(temp_node.left)
                sum_path.append(temp_node.left.val+temp_val)
        
        return False