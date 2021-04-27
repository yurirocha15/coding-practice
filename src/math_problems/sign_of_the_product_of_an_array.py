#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1822. Sign of the Product of an Array
URL: https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
"""
from typing import List


class Solution:
    def array_sign(self, nums: List[int]) -> int:
        ret = 1
        for n in nums:
            if not n:
                return 0
            if n < 0:
                ret *= -1
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.array_sign(nums=[-1, -2, -3, -4, 3, 2, 1]) == 1
    assert solution.array_sign(nums=[1, 5, 0, 2, -3]) == 0
    assert solution.array_sign(nums=[-1, 1, -1, 1, -1]) == -1
