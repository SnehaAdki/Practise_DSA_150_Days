#  Find Common Characters
# https://leetcode.com/problems/find-common-characters/submissions/1833349168/

# 1002. Find Common Characters
# Easy
# Topics
# premium lock icon
# Companies
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
 

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]


def count_char(arr):
    final_res = []
    final_dict = {}
    for i in range(0,len(arr)):
        temp_map = {}
        for j in range(0,len(arr[i])):
            temp_map[arr[i][j]]=temp_map.get(arr[i][j],0)+1
            # temp_map[arr[i][j]]=min(val_curr,temp_map.get(arr[i][j],1))
        if len(final_dict) > 0:
            for k,v in final_dict.items():
                final_dict[k] = min(final_dict[k],temp_map.get(k,0))
        else:
            final_dict = temp_map
        
    for k,v in final_dict.items():
        if v!=0:
            final_res.extend([k]*v)
       
    print(final_res) 

arr = ["bella","label","roller"]
count_char(arr)