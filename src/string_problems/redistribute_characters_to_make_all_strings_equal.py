#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1897. Redistribute Characters to Make All Strings Equal
URL: https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/
"""

from collections import Counter
from typing import List


class Solution:
    def make_equal(self, words: List[str]) -> bool:
        return all(x % len(words) == 0 for x in Counter("".join(words)).values())


if __name__ == "__main__":
    solution = Solution()
    assert solution.make_equal(words=["abc", "aabc", "bc"])
    assert not solution.make_equal(words=["ab", "a"])
