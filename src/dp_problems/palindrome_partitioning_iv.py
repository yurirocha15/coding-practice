#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1745. Palindrome Partitioning IV
URL: https://leetcode.com/problems/palindrome-partitioning-iv/description/
"""


class Solution:
    def check_partitioning(self, s: str) -> bool:
        def isPalindrome(s: str):
            return s == s[::-1]

        n = len(s)
        for i in range(1, n):
            for j in range(i + 1, n):
                if isPalindrome(s[:i]) and isPalindrome(s[i:j]) and isPalindrome(s[j:]):
                    return True
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.check_partitioning(s="abcbdd") is True
    assert solution.check_partitioning(s="bcbddxy") is False
