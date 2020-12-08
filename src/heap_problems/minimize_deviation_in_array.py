#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1675. Minimize Deviation in Array
URL: https://leetcode.com/problems/minimize-deviation-in-array/

Description:
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

Example 1:
Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

Example 2:
Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.

Example 3:
Input: nums = [2,10,8]
Output: 3

Constraints:

n == nums.length
2 <= n <= 105
1 <= nums[i] <= 109

Complexity:
Time: O(n log n log max_num)
Space: O(n)
"""

import heapq
from typing import List


class Solution:
    # our objective is to make the maximum value and the minimum value as close as possible
    def minimum_deviation(self, nums: List[int]) -> int:
        # need to make the numbers negative so the heap[0]
        # position can store the maximum value
        # we multiply the even numbers by two so every number will be
        # on their upper bound
        nums = [-n << (n & 1) for n in nums]  # O(n)
        orig_len = len(nums)
        # get the current smallest value
        min_n = -max(nums)
        # start the heap
        heapq.heapify(nums)
        ret = 10_000_000_000
        # if the number we popped cannot be pushed again
        # there is no optimizations remaining
        while len(nums) == orig_len:  # O(n log max_num)
            # get the current maximum value
            max_n = -heapq.heappop(nums)  # O(log n)
            # to get the deviation, we just need the
            # smallest and the biggest value on the array
            ret = min(ret, max_n - min_n)
            # if the current maximum is not an odd number
            # we divide it by two, calculate the new minimum value
            # and push it into the heap
            if not max_n & 1:
                max_n >>= 1
                min_n = min(min_n, max_n)
                heapq.heappush(nums, -max_n)  # O(log n)
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimum_deviation([1, 2, 3, 4]) == 1
    assert solution.minimum_deviation([4, 1, 5, 20, 3]) == 3
    assert solution.minimum_deviation([2, 10, 8]) == 3
