# @l2g 1930 python3
# [1930] Unique Length-3 Palindromic Subsequences
# Difficulty: Medium
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences
#
# Given a string s,
# return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence,
# it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
#
#
# Example 1:
#
# Input: s = "aabca"
# Output: 3
# Explanation: The 3 palindromic subsequences of length 3 are:
# - "aba" (subsequence of "aabca")
# - "aaa" (subsequence of "aabca")
# - "aca" (subsequence of "aabca")
#
# Example 2:
#
# Input: s = "adc"
# Output: 0
# Explanation: There are no palindromic subsequences of length 3 in "adc".
#
# Example 3:
#
# Input: s = "bbcbaba"
# Output: 4
# Explanation: The 4 palindromic subsequences of length 3 are:
# - "bbb" (subsequence of "bbcbaba")
# - "bcb" (subsequence of "bbcbaba")
# - "bab" (subsequence of "bbcbaba")
# - "aba" (subsequence of "bbcbaba")
#
#
# Constraints:
#
# 3 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#

import string


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        cnt = 0
        outer_index = {c: [-1, -1] for c in string.ascii_lowercase}
        for i, c in enumerate(s):
            if outer_index[c][0] == -1 or i < outer_index[c][0]:
                outer_index[c][0] = i
            elif i > outer_index[c][1]:
                outer_index[c][1] = i

        for idx in outer_index.values():
            if idx[0] != -1 and idx[1] != -1:
                cnt += len(set(s[idx[0] + 1 : idx[1]]))
        return cnt


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1930.py")])
