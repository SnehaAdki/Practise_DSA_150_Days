# Binary Tree Paths

# https://leetcode.com/problems/binary-tree-paths/submissions/1840427182/

# 257. Binary Tree Paths
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.


# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# Example 2:
# Input: root = [1]
# Output: ["1"]


# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(node,path):
            if node == None:
                return None
            dfs(node.left,f"{path}->{node.val}")
            dfs(node.right,f"{path}->{node.val}")
            if not (node.left or node.right):
                result.append(f"{path}->{node.val}")
        dfs(root,'')
        return [ i[2:] for i in result]