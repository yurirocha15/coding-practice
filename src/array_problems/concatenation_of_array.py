#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1929. Concatenation of Array
URL: https://leetcode.com/problems/concatenation-of-array/description/
"""

from typing import List


class Solution:
    def get_concatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == "__main__":
    solution = Solution()
    assert solution.get_concatenation(nums=[1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert solution.get_concatenation(nums=[1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
