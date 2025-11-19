# Middle of the Linked List

# https://leetcode.com/problems/middle-of-the-linked-list/submissions/1834480154/

# 876. Middle of the Linked List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.



# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        fast = head
        slow = head.next

        while slow and slow.next != None:
            slow = slow.next.next
            fast = fast.next

        return fast if slow is None else fast.next