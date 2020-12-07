#!/usr/bin/env python
"""
Platform: LeetCode
1663. Smallest String With A Given Numeric Value
URL: https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

Description:
The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet,
so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values.
For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order,
that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

Example 1:
Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.

Example 2:
Input: n = 5, k = 73
Output: "aaszz"

Constraints:

1 <= n <= 10^5
n <= k <= 26 * n

Complexity:
Time: O(1)
Space: O(N)
"""


class Solution:
    def get_smallest_string(self, n: int, k: int) -> str:
        ret = ""
        # start calculating how many a's we can put
        curr_char = 1
        # we only loop until letter y to avoid division by 0
        while curr_char < 26 and k > 0:
            char_cnt = ((26 * n) - k) // (26 - curr_char)
            k -= char_cnt * curr_char
            # 97 is the ASCII code for letter 'a'. We use 96 because curr_char starts from 1
            ret += chr(96 + curr_char) * char_cnt
            n -= char_cnt
            curr_char += 1
        # here we add the remaining letter z's
        return ret + "z" * n
