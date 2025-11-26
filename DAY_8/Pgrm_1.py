# Subtree of Another Tree

# https://leetcode.com/problems/subtree-of-another-tree/submissions/1838504787/

# 572. Subtree of Another Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


# Example 1:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Example 2:
# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def find_sub_tree(self,root,subroot):
        if not root and not subroot:
            return True

        if not root or not subroot:
            return False

        if root.val != subroot.val:
            return False

        return (
            self.find_sub_tree(root.left,subroot.left) and
            self.find_sub_tree(root.right,subroot.right)
        )
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        
        if self.find_sub_tree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)