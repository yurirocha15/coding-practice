# @l2g 1822 python3
# [1822] Sign of the Product of an Array
# Difficulty: Easy
# https://leetcode.com/problems/sign-of-the-product-of-an-array
#
# There is a function signFunc(x) that returns:
#
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
#
# You are given an integer array nums. Let product be the product of all values in the array nums.
# Return signFunc(product).
#
# Example 1:
#
# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1
#
# Example 2:
#
# Input: nums = [1,5,0,2,-3]
# Output: 0
# Explanation: The product of all values in the array is 0, and signFunc(0) = 0
#
# Example 3:
#
# Input: nums = [-1,1,-1,1,-1]
# Output: -1
# Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# -100 <= nums[i] <= 100
#
#
from functools import reduce
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # ret = 1
        # for n in nums:
        #     if not n:
        #         return 0
        #     if n < 0:
        #         ret *= -1
        # return ret
        return reduce(lambda a, b: a if b > 0 else (-a if b < 0 else 0), [1] + nums)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1822.py")])
