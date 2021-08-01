# @l2g 1745 python3
# [1745] Palindrome Partitioning IV
# Difficulty: Hard
# https://leetcode.com/problems/palindrome-partitioning-iv
#
# Given a string s,
# return true if it is possible to split the string s into three non-empty palindromic substrings.
# Otherwise,return false.​​​​​
# A string is said to be palindrome if it the same string when reversed.
#
# Example 1:
#
# Input: s = "abcbdd"
# Output: true
# Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
#
# Example 2:
#
# Input: s = "bcbddxy"
# Output: false
# Explanation: s cannot be split into 3 palindromes.
#
#
# Constraints:
#
# 3 <= s.length <= 2000
# s​​​​​​ consists only of lowercase English letters.
#
#


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def isPalindrome(s: str):
            return s == s[::-1]

        n = len(s)
        for i in range(1, n):
            for j in range(i + 1, n):
                if isPalindrome(s[:i]) and isPalindrome(s[i:j]) and isPalindrome(s[j:]):
                    return True
        return False


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1745.py")])
