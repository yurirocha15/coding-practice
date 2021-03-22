#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1784. Check if Binary String Has at Most One Segment of Ones
URL: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description/
"""


class Solution:
    def check_ones_segment(self, s: str) -> bool:
        return "01" not in s


if __name__ == "__main__":
    solution = Solution()
    assert not solution.check_ones_segment(s="1001")
    assert solution.check_ones_segment(s="110")
