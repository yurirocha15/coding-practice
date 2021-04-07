#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1802. Maximum Value at a Given Index in a Bounded Array
URL: https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/
"""


class Solution:
    def max_value(self, n: int, index: int, maxSum: int) -> int:
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
    solution = Solution()
    assert solution.max_value(n=4, index=2, maxSum=6) == 2
    assert solution.max_value(n=6, index=1, maxSum=10) == 3
