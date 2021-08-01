# @l2g 1856 python3
# [1856] Maximum Subarray Min-Product
# Difficulty: Medium
# https://leetcode.com/problems/maximum-subarray-min-product
#
# The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.
#
# For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
#
# Given an array of integers nums,return the maximum min-product of any non-empty subarray of nums.
# Since the answer may be large,return it modulo 10^9 + 7.
# Note that the min-product should be maximized before performing the modulo operation.
# Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.
# A subarray is a contiguous part of an array.
#
# Example 1:
#
# Input: nums = [1,2,3,2]
# Output: 14
# Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
# 2 * (2+3+2) = 2 * 7 = 14.
#
# Example 2:
#
# Input: nums = [2,3,3,1,2]
# Output: 18
# Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
# 3 * (3+3) = 3 * 6 = 18.
#
# Example 3:
#
# Input: nums = [3,1,5,6,4,2]
# Output: 60
# Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
# 4 * (5+6+4) = 4 * 15 = 60.
#
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^7
#
#


#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#
# https://leetcode.com/problems/maximum-subarray-min-product/description/
#
# algorithms
# Medium (38.52%)
# Total Accepted:    6.4K
# Total Submissions: 16.8K
# Testcase Example:  '[1,2,3,2]'
#
# The min-product of an array is equal to the minimum value in the array
# multiplied by the array's sum.
#
#
# For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 *
# (3+2+5) = 2 * 10 = 20.
#
#
# Given an array of integers nums, return the maximum min-product of any
# non-empty subarray of nums. Since the answer may be large, return it modulo
# 10^9 + 7.
#
# Note that the min-product should be maximized before performing the modulo
# operation. Testcases are generated such that the maximum min-product without
# modulo will fit in a 64-bit signed integer.
#
# A subarray is a contiguous part of an array.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,2]
# Output: 14
# Explanation: The maximum min-product is achieved with the subarray [2,3,2]
# (minimum value is 2).
# 2 * (2+3+2) = 2 * 7 = 14.
#
#
# Example 2:
#
#
# Input: nums = [2,3,3,1,2]
# Output: 18
# Explanation: The maximum min-product is achieved with the subarray [3,3]
# (minimum value is 3).
# 3 * (3+3) = 3 * 6 = 18.
#
#
# Example 3:
#
#
# Input: nums = [3,1,5,6,4,2]
# Output: 60
# Explanation: The maximum min-product is achieved with the subarray [5,6,4]
# (minimum value is 4).
# 4 * (5+6+4) = 4 * 15 = 60.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^7
#
#
#

from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        pre_sum = [0] + list(accumulate(nums))
        dq = deque()
        res = 0
        for i in range(len(nums) + 1):
            while dq and (i == len(nums) or nums[dq[-1]] > nums[i]):
                j = dq.pop()
                res = max(
                    res, nums[j] * (pre_sum[i] - pre_sum[dq[-1] + 1 if dq else 0])
                )
            dq.append(i)
        return res % (10 ** 9 + 7)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1856.py")])
