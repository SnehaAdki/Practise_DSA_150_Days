# Cousins in Binary Tree
# https://leetcode.com/problems/cousins-in-binary-tree/submissions/1840447487/
# 993. Cousins in Binary Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins if they have the same depth with different parents.

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.


# Example 1:
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false

# Example 2:
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true

# Example 3:
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false



from typing import Optional


class TreeNode:
    def __init__(self, data = 0,left = None,right = None):
        self.left = left
        self.right = right
        self.data = data
        
class Solution:
    def isCousins(self,root:Optional[TreeNode],x: int,y: int)-> bool:
        if root == None:
            return False
        def get_level_parent(node,parent,value,level):
            if node == None :
                return None
            if node.val == value:
                return (level,parent)
            return get_level_parent(node.left, node, value , level+1) or get_level_parent(node.right, node, value , level+1)
            
        level_x , parent_x = get_level_parent(root,None,x,0)
        level_y , parent_y = get_level_parent(root,None,y,0)
        
        return level_y == level_x and parent_y!= parent_x