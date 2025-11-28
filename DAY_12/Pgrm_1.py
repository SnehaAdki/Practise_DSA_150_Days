# Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/submissions/1841721888/

# 1108. Defanging an IP Address
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".


# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# Example 2:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

class Solution:
    def defangIPaddr(self, address: str) -> str:
        add_list = list(address)

        for i in range(0,len(add_list)):
            if add_list[i] == '.':
                add_list[i] = '[.]'

        return ''.join(add_list)