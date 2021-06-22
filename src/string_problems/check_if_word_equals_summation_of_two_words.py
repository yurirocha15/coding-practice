#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1880. Check if Word Equals Summation of Two Words
URL: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description/
"""


class Solution:
    def convert(self, word: str) -> int:
        exp = 1
        ret = 0
        for n in reversed(word):
            ret += (ord(n) - 97) * exp
            exp *= 10
        return ret

    def is_sum_equal(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.convert(firstWord) + self.convert(secondWord) == self.convert(
            targetWord
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.is_sum_equal(firstWord="acb", secondWord="cba", targetWord="cdb")
    assert not solution.is_sum_equal(firstWord="aaa", secondWord="a", targetWord="aab")
    assert solution.is_sum_equal(firstWord="aaa", secondWord="a", targetWord="aaaa")
