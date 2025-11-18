# Sum of All Odd Length Subarrays

# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/1833389904/

# 1588. Sum of All Odd Length Subarrays
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

# A subarray is a contiguous subsequence of the array.


# Example 1:
# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

# Example 2:
# Input: arr = [1,2]
# Output: 3
# Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

# Example 3:
# Input: arr = [10,11,12]
# Output: 66



def prefix_sum(arr):
    
    prefix_sum = [arr[0]]
    sum = arr[0]
    for i in range(1,len(arr)):
        sum +=arr[i]
        prefix_sum.append(prefix_sum[i-1] + arr[i])

    for i in range(2,len(arr),2):
        j =0
        while j+i < len(arr):
            if j==0:
                sum+=prefix_sum[i]
            else:
                sum+=(prefix_sum[i+j]-prefix_sum[j-1])
            j=j+1
    return sum

arr = [1,4,2,5,3]
print(prefix_sum(arr))







