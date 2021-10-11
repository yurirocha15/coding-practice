# @l2g 2016 python3
# [2016] Maximum Difference Between Increasing Elements
# Difficulty: Easy
# https://leetcode.com/problems/maximum-difference-between-increasing-elements
#
# Given a 0-indexed integer array nums of size n,
# find the maximum difference between nums[i] and nums[j] (i.e.,nums[j] - nums[i]),
# such that 0 <= i < j < n and nums[i] < nums[j].
# Return the maximum difference. If no such i and j exists, return -1.
#
# Example 1:
#
# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0,the difference nums[j] - nums[i] = 7 - 1 = 6,but i > j,
# so it is not valid.
#
# Example 2:
#
# Input: nums = [9,4,3,2]
# Output: -1
# Explanation:
# There is no i and j such that i < j and nums[i] < nums[j].
#
# Example 3:
#
# Input: nums = [1,5,2,10]
# Output: 9
# Explanation:
# The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
#
#
# Constraints:
#
# n == nums.length
# 2 <= n <= 1000
# 1 <= nums[i] <= 10^9
#
#

from typing import List, Optional


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ret: int = -1
        cur_min: Optional[int] = None
        for n in nums:
            if not cur_min or n < cur_min:
                cur_min = n
            else:
                ret = max(ret, n - cur_min)
        return ret


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_2016.py")])
