#!/usr/bin/env python
"""
Platform: LeetCode
1736. Latest Time by Replacing Hidden Digits
URL: https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

Description:
You are given a string time in the form of hh:mm,
where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get
from time by replacing the hidden digits.

Example 1:
Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the
digit '2' is 23 and the latest minute ending with the digit '0' is 50.

Example 2:
Input: time = "0?:3?"
Output: "09:39"

Example 3:
Input: time = "1?:22"
Output: "19:22"

Constraints:
2 <= n <= 10^4
encoded.length == n - 1
0 <= encoded[i] <= 10^5
0 <= first <= 10^5
"""


class Solution:
    def maximum_time(self, time: str) -> str:
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
    solution = Solution()
    assert solution.maximum_time("2?:?0") == "23:50"
    assert solution.maximum_time("0?:3?") == "09:39"
    assert solution.maximum_time("1?:22") == "19:22"
