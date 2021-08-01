# @l2g 1736 python3
# [1736] Latest Time by Replacing Hidden Digits
# Difficulty: Easy
# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits
#
# You are given a string time in the form of  hh:mm,
# where some of the digits in the string are hidden (represented by ?).
# The valid times are those inclusively between 00:00 and 23:59.
# Return the latest valid time you can get from time by replacing the hidden digits.
#
# Example 1:
#
# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
#
# Example 2:
#
# Input: time = "0?:3?"
# Output: "09:39"
#
# Example 3:
#
# Input: time = "1?:22"
# Output: "19:22"
#
#
# Constraints:
#
# time is in the format hh:mm.
# It is guaranteed that you can produce a valid time from the given string.
#
#


class Solution:
    def maximumTime(self, time: str) -> str:
        ret = ""
        for i in range(len(time)):
            c = time[i]
            if c == "?":
                if i == 0:
                    c = "2" if time[i + 1] in "0123?" else "1"
                elif i == 1:
                    c = "3" if ret[i - 1] == "2" else "9"
                elif i == 3:
                    c = "5"
                else:
                    c = "9"
            ret += c
        return ret


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1736.py")])
