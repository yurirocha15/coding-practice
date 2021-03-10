#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1771. Maximize Palindrome Length From Subsequences
URL: https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/description/
"""
from functools import lru_cache


class Solution:
    def longest_palindrome(self, word1: str, word2: str) -> int:
        word = word1 + word2

        @lru_cache(None)
        def dp(left: int, right: int):
            if right == left:
                return 1
            if right < left:
                return 0
            if word[left] == word[right]:
                return 2 + dp(left + 1, right - 1)
            return max(dp(left + 1, right), dp(left, right - 1))

        ret = 0
        for letter in "abcdefghijklmnopqrstuvwxyz":
            left = word1.find(letter)
            right = word2.rfind(letter)
            if left != -1 and right != -1:
                ret = max(ret, dp(left, len(word1) + right))

        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.longest_palindrome(word1="cacb", word2="cbba") == 5
    assert solution.longest_palindrome(word1="ab", word2="ab") == 3
    assert solution.longest_palindrome(word1="aa", word2="bb") == 0
