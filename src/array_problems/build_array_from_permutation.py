#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1920. Build Array from Permutation
URL: https://leetcode.com/problems/build-array-from-permutation/description/
"""

from typing import List


class Solution:
    def build_array(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


if __name__ == "__main__":
    solution = Solution()
    assert solution.build_array(nums=[0, 2, 1, 5, 3, 4]) == [0, 1, 2, 4, 5, 3]
    assert solution.build_array(nums=[5, 0, 1, 2, 3, 4]) == [4, 5, 0, 1, 2, 3]
