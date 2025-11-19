# Remove Duplicates from Sorted List

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/1834438681/

# 83. Remove Duplicates from Sorted List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        temp = head
        while temp and temp.next!= None:
            del_node = temp.next
            print("----")
            if del_node.val == temp.val:
                temp.next = del_node.next
                del_node.next = None
            temp=temp.next

        return head