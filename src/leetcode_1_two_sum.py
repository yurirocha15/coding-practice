# @l2g 1 python3
# [1] Two Sum
# Difficulty: Easy
# https://leetcode.com/problems/two-sum
#
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, n in enumerate(nums):
            remaining = target - n
            if remaining in complement:
                return [i, complement[remaining]]
            complement[n] = i
        return [0, 1]


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1.py")])
