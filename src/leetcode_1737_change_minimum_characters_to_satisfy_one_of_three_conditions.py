# @l2g 1737 python3
# [1737] Change Minimum Characters to Satisfy One of Three Conditions
# Difficulty: Medium
# https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions
#
# You are given two strings a and b that consist of lowercase letters.In one operation,
# you can change any character in a or b to any lowercase letter.
# Your goal is to satisfy one of the following three conditions:
#
# Every letter in a is strictly less than every letter in b in the alphabet.
# Every letter in b is strictly less than every letter in a in the alphabet.
# Both a and b consist of only one distinct letter.
#
# Return the minimum number of operations needed to achieve your goal.
#
# Example 1:
#
# Input: a = "aba", b = "caa"
# Output: 2
# Explanation: Consider the best way to make each condition true:
# 1) Change b to "ccc" in 2 operations, then every letter in a is less than every letter in b.
# 2) Change a to "bbb" and b to "aaa" in 3 operations,
# then every letter in b is less than every letter in a.
# 3) Change a to "aaa" and b to "aaa" in 2 operations, then a and b consist of one distinct letter.
# The best way was done in 2 operations (either condition 1 or condition 3).
#
# Example 2:
#
# Input: a = "dabadd", b = "cda"
# Output: 3
# Explanation: The best way is to make condition 1 true by changing b to "eee".
#
#
# Constraints:
#
# 1 <= a.length, b.length <= 10^5
# a and b consist only of lowercase letters.
#
#

from typing import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        ca = Counter(a)
        cb = Counter(b)
        suma = sum(ca.values())
        sumb = sum(cb.values())
        ret = len(a) + len(b) - max((ca + cb).values())
        for c in "bcdefghijklmnopqrstuvwxyz":
            cnta = cntb = 0
            for cca, vca in ca.items():
                if cca < c:
                    cntb += vca
                else:
                    cnta += vca
            for ccb, vcb in cb.items():
                if ccb < c:
                    cnta += vcb
                else:
                    cntb += vcb

            ret = min([ret, cnta, cntb])
        return ret


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1737.py")])
