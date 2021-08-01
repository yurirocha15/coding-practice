# @l2g 1898 python3
# [1898] Maximum Number of Removable Characters
# Difficulty: Medium
# https://leetcode.com/problems/maximum-number-of-removable-characters
#
# You are given two strings s and p where p is a subsequence of s.
# You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).
# You want to choose an integer k (0 <= k <= removable.length) such that,
# after removing k characters from s using the first k indices in removable,
# p is still a subsequence of s.More formally,
# you will mark the character at s[removable[i]] for each 0 <= i < k,
# then remove all marked characters and check if p is still a subsequence.
# Return the maximum k you can choose such that p is still a subsequence of s after the removals.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
# Example 1:
#
# Input: s = "abcacb", p = "ab", removable = [3,1,0]
# Output: 2
# Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
# "ab" is a subsequence of "accb".
# If we remove the characters at indices 3,1,and 0,"abcacb" becomes "ccb",
# and "ab" is no longer a subsequence.
# Hence, the maximum k is 2.
#
# Example 2:
#
# Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
# Output: 1
# Explanation: After removing the character at index 3, "abcbddddd" becomes "abcddddd".
# "abcd" is a subsequence of "abcddddd".
#
# Example 3:
#
# Input: s = "abcab", p = "abc", removable = [0,1,2,3,4]
# Output: 0
# Explanation: If you remove the first index in the array removable, "abc" is no longer a subsequence.
#
#
# Constraints:
#
# 1 <= p.length <= s.length <= 10^5
# 0 <= removable.length < s.length
# 0 <= removable[i] < s.length
# p is a subsequence of s.
# s and p both consist of lowercase English letters.
# The elements in removable are distinct.
#
#

from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(k: int) -> bool:
            p_idx = s_idx = 0
            unavailable = set(removable[:k])
            while s_idx < len(s):
                if s_idx in unavailable:
                    s_idx += 1
                    continue
                if p[p_idx] == s[s_idx]:
                    p_idx += 1
                if p_idx == len(p):
                    return True
                s_idx += 1
            return False

        left = 0
        right = len(removable)

        while left < right:
            middle = (left + right) // 2
            if is_subsequence(middle + 1):
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1898.py")])
