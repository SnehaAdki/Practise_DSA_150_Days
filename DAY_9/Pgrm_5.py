# Range Sum of BST

# https://leetcode.com/problems/range-sum-of-bst/submissions/1841017974/

# 938. Range Sum of BST
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


# Example 1:
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.



from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # approach1 via DFS (recursion)
    def range_sun_DFS(self, root: Optional[TreeNode], low: int, high: int) -> int:

        total_val = 0
        def dfs(node):
            if node == None:
                return 0
            c_v = 0
            if node.val >= low and node.val <= high:
                c_v = node.val
            ls = dfs(node.left)
            rs = dfs(node.right)
            return c_v+ls+rs
        
        dfs(root)
        return total_val
    
    
    # approach2 BFS (stack)
    def range_sun_DFS(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total_val = 0
        if root == None : 
            return total_val
        stack_all = [root]
        
        while len(stack_all)!=0:
            node = stack_all.pop()
            
            if node.val >= low and node.val <= high: 
                total_val += node.val
            
            if node.left:
                stack_all.append(node.left)
            
            if node.right:
                stack_all.append(node.right)
                
        return total_val
    
    