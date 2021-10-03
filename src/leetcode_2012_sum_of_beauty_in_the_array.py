# @l2g 2012 python3
# [2012] Sum of Beauty in the Array
# Difficulty: Medium
# https://leetcode.com/problems/sum-of-beauty-in-the-array
#
# You are given a 0-indexed integer array nums.For each index i (1 <= i <= nums.
# length - 2) the beauty of nums[i] equals:
#
# 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
# 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
# 0, if none of the previous conditions holds.
#
# Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.
#
# Example 1:
#
# Input: nums = [1,2,3]
# Output: 2
# Explanation: For each index i in the range 1 <= i <= 1:
# - The beauty of nums[1] equals 2.
#
# Example 2:
#
# Input: nums = [2,4,6,4]
# Output: 1
# Explanation: For each index i in the range 1 <= i <= 2:
# - The beauty of nums[1] equals 1.
# - The beauty of nums[2] equals 0.
#
# Example 3:
#
# Input: nums = [3,2,1]
# Output: 0
# Explanation: For each index i in the range 1 <= i <= 1:
# - The beauty of nums[1] equals 0.
#
#
# Constraints:
#
# 3 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
#
#
import math
from typing import List


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        res: int = 0
        n: int = len(nums)
        left: List[int] = [2] * n
        right: List[int] = [2] * n
        m_left, m_right = nums[0], nums[-1]
        for i in range(1, n - 1):
            m_left = max(m_left, nums[i - 1])
            m_right = min(m_right, nums[n - i])
            left[i] = left[i] - int(nums[i] <= m_left) - int(nums[i] <= nums[i - 1])
            right[n - i - 1] = (
                right[n - i - 1]
                - int(nums[n - i - 1] >= m_right)
                - int(nums[n - i - 1] >= nums[n - i])
            )
        for a, b in zip(left[1:-1], right[1:-1]):
            res += min(a, b)
        return res


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2012.py")])
