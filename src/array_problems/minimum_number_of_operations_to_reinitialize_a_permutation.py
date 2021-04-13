#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1806. Minimum Number of Operations to Reinitialize a Permutation
URL: https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/description/
"""


class Solution:
    def reinitialize_permutation(self, n: int) -> int:
        idx: int = 1
        ret: int = 0
        while ret == 0 or idx != 1:
            idx *= 2
            if idx >= n:
                idx -= n - 1
            ret += 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.reinitialize_permutation(n=2) == 1
    assert solution.reinitialize_permutation(n=4) == 2
    assert solution.reinitialize_permutation(n=6) == 4
