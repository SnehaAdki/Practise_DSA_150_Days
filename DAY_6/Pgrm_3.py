# Valid Parentheses

# https://leetcode.com/problems/valid-parentheses/submissions/1835279218/

# 20. Valid Parentheses
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false



def isValidate(s):
    dict_val = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    stack = []
    for i in s:
        if i in dict_val.keys() and len(stack) > 0:
            if stack[-1] == dict_val[i]:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
    return True if len(stack) ==0 else False
    
isValidate("()")
isValidate("()[]{}")
isValidate("(]")
isValidate( "([])")
    