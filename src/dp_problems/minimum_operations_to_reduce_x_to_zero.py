#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1658. Minimum Operations to Reduce X to Zero
URL: https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

Description:
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.


Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4
1 <= x <= 10^9

Complexity:
Time: O(N)
Space: O(N)
"""
from typing import List


class Solution:
    def min_operations(self, nums: List[int], x: int) -> int:
        if not x:
            return x
        # will store the forward sums
        memoization = dict()
        # initialize for the 0 case
        memoization[0] = 0
        tmp_sum, ops = 0, 0
        # forward sum, will store the corresponding number of opperations to obtain a given intermediate sum
        for n in nums:
            tmp_sum, ops = tmp_sum + n, ops + 1
            # no need to compute values bigger than x
            if tmp_sum > x:
                break
            memoization[tmp_sum] = ops
        # corner cases for speed up
        # if the total sum is smaller than x, it is impossible
        if tmp_sum < x:
            return -1
        # if the total sum is equal x, ops is the array length
        if tmp_sum == x:
            return ops
        # loop through the vector backwards, calculating the intermediate sum and looking for the complement in the forward sum dict
        ret, cnt = -1, 0
        for n in reversed(nums):
            if x < 0:
                return ret
            if x in memoization and (ret < 0 or memoization[x] + cnt < ret):
                ret = memoization[x] + cnt
            x, cnt = x - n, cnt + 1

        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.min_operations([1, 1, 4, 2, 3], 5) == 2
    assert solution.min_operations([5, 6, 7, 8, 9], 4) == -1
    assert solution.min_operations([3, 2, 20, 1, 1, 3], 10) == 5
