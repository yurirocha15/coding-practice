#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1881. Maximum Value after Insertion
URL: https://leetcode.com/problems/maximum-value-after-insertion/description/
"""


class Solution:
    def max_value(self, n: str, x: int) -> str:
        for i, c in enumerate(n):
            if c != "-" and (
                (n[0] == "-" and int(c) > x) or (n[0] != "-" and int(c) < x)
            ):
                return n[:i] + str(x) + n[i:]
        return n + str(x)


if __name__ == "__main__":
    solution = Solution()
    assert solution.max_value(n="99", x=9) == "999"
    assert solution.max_value(n="-13", x=2) == "-123"
