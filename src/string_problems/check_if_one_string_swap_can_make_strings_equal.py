#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1790. Check if One String Swap Can Make Strings Equal
URL: https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/
"""


class Solution:
    def are_almost_equal(self, s1: str, s2: str) -> bool:
        if sorted(s1) != sorted(s2):
            return False

        return sum(map(lambda c1, c2: c1 != c2, s1, s2)) in [0, 2]


if __name__ == "__main__":
    solution = Solution()
    assert solution.are_almost_equal(s1="bank", s2="kanb")
    assert not solution.are_almost_equal(s1="attack", s2="defend")
    assert solution.are_almost_equal(s1="kelb", s2="kelb")
    assert not solution.are_almost_equal(s1="abcd", s2="dcba")
