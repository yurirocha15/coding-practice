# @l2g 1784 python3
# [1784] Check if Binary String Has at Most One Segment of Ones
# Difficulty: Easy
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones
#
# Given a binary string s ​​​​​without leading zeros,
# return true​​​ if s contains at most one contiguous segment of ones.Otherwise,return false.
#
# Example 1:
#
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.
#
# Example 2:
#
# Input: s = "110"
# Output: true
#
# Constraints:
#
# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.
#
#


class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1784.py")])
