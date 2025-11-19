# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1834474896/

# 21. Merge Two Sorted Lists
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        t1 = list1
        t2 = list2
        result = ListNode()

        while t1 != None and t2!= None:
            if t1.val < t2.val:
                temp = ListNode(t1.val)
                r1 = result
                while r1.next != None:
                    r1 = r1.next
                r1.next = temp
                t1 = t1.next
            else:
                temp = ListNode(t2.val)
                r1 = result
                while r1.next != None:
                    r1 = r1.next
                r1.next = temp
                t2 = t2.next

        if t1:
            r1 = result
            while r1.next != None:
                r1 = r1.next
            r1.next = t1
            
        if t2:
            r1 = result
            while r1.next != None:
                r1 = r1.next
            r1.next = t2
        return result.next