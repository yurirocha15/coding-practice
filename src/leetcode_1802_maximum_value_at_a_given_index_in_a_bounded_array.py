# @l2g 1802 python3
# [1802] Maximum Value at a Given Index in a Bounded Array
# Difficulty: Medium
# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array
#
# You are given three positive integers: n,index,and maxSum.
# You want to construct an array nums (0-indexed) that satisfies the following conditions:
#
# nums.length == n
# nums[i] is a positive integer where 0 <= i < n.
# abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# The sum of all the elements of nums does not exceed maxSum.
# nums[index] is maximized.
#
# Return nums[index] of the constructed array.
# Note that abs(x) equals x if x >= 0, and -x otherwise.
#
# Example 1:
#
# Input: n = 4, index = 2,  maxSum = 6
# Output: 2
# Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
# There are no arrays that satisfy all the conditions and have nums[2] == 3,
# so 2 is the maximum nums[2].
#
# Example 2:
#
# Input: n = 6, index = 1,  maxSum = 10
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= maxSum <= 10^9
# 0 <= index < n
#
#


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n
        left: int = 0
        right: int = maxSum + 1
        ret: int = 0

        def isValidArray(target: int, n: int, index: int, maxSum: int) -> bool:
            first_half: int = (
                (2 * target - index) * (index + 1)
                if target > index
                else (target + 1) * target
            )
            second_half: int = (
                (n - index - 1) * (2 * target + index - n)
                if target > n - index
                else (target - 1) * target
            )
            return (first_half + second_half) / 2 <= maxSum

        while left < right - 1:
            target: int = (right + left) // 2
            if isValidArray(target, n, index, maxSum):
                ret = max(ret, target)
                left = target
            else:
                right = target
        return ret + 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1802.py")])
