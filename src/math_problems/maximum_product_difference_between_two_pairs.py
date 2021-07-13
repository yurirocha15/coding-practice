#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1913. Maximum Product Difference Between Two Pairs
URL: https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
"""

from typing import List


class Solution:
    def max_product_difference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.max_product_difference(nums=[5, 6, 2, 7, 4]) == 34
    assert solution.max_product_difference(nums=[4, 2, 5, 9, 7, 4, 8]) == 64
