#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1770. Maximum Score from Performing Multiplication Operations
URL: https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description/
"""
from functools import lru_cache
from typing import List


class Solution:
    def maximum_score(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(None)
        def dp(left: int, right: int, idx: int) -> int:
            if idx >= len(multipliers):
                return 0
            return max(
                dp(left + 1, right, idx + 1) + (multipliers[idx] * nums[left]),
                dp(left, right - 1, idx + 1) + (multipliers[idx] * nums[right]),
            )

        return dp(0, len(nums) - 1, 0)


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximum_score(nums=[1, 2, 3], multipliers=[3, 2, 1]) == 14
    assert (
        solution.maximum_score(
            nums=[-5, -3, -3, -2, 7, 1], multipliers=[-10, -5, 3, 4, 6]
        )
        == 102
    )
