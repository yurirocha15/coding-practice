# @l2g 1758 python3
# [1758] Minimum Changes To Make Alternating Binary String
# Difficulty: Easy
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string
#
# You are given a string s consisting only of the characters '0' and '1'.In one operation,
# you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal.For example,
# the string "010" is alternating,while the string "0100" is not.
# Return the minimum number of operations needed to make s alternating.
#
# Example 1:
#
# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.
#
# Example 2:
#
# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
#
# Example 3:
#
# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".
#
#
# Constraints:
#
# 1 <= s.length <= 10^4
# s[i] is either '0' or '1'.
#
#


class Solution:
    def minOperations(self, s: str) -> int:
        # check considering first number = 0
        last_char = "1"
        cnt_1 = 0
        for c in s:
            if c == last_char:
                cnt_1 += 1
            last_char = "1" if last_char == "0" else "0"
        # check considering first number = 1
        last_char = "0"
        cnt_2 = 0
        for c in s:
            if c == last_char:
                cnt_2 += 1
            last_char = "1" if last_char == "0" else "0"
        return min(cnt_1, cnt_2)


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1758.py")])
