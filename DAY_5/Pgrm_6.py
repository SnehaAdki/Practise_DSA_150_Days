# Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/submissions/1834497823/

# 234. Palindrome Linked List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# # Input: head = [1,2]
# Output: false


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self,h1):
        curr = h1
        prev = None

        while curr != None:
            h1 = curr
            curr = curr.next
            h1.next = prev
            prev = h1

        return h1


    def isPalindrome(self, head):
        ot = org_arr = ListNode()
        temp = head
        while temp!=None:
            ot.next = ListNode(temp.val)
            ot = ot.next
            temp = temp.next

        reverse_head = self.reverse(head)
        ot = org_arr.next
        rh = reverse_head
        while ot != None and rh!= None:
            print(ot.val)
            print(rh.val)
            if ot.val != rh.val:
                return False
            ot = ot.next
            rh = rh.next
        return True 
        
