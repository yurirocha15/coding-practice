#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1805. Number of Different Integers in a String
URL: https://leetcode.com/problems/number-of-different-integers-in-a-string/description/
"""
import re


class Solution:
    def num_different_integers(self, word: str) -> int:
        return len(set(map(int, re.sub("[^0-9]+", " ", word).split())))


if __name__ == "__main__":
    solution = Solution()
    assert solution.num_different_integers(word="a123bc34d8ef34") == 3
    assert solution.num_different_integers(word="leet1234code234") == 2
    assert solution.num_different_integers(word="a1b01c001") == 1
