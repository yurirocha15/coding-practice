#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1832. Check if the Sentence Is Pangram
URL: https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
"""


# O(N) / O(1)
class Solution:
    def check_if_pangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


if __name__ == "__main__":
    solution = Solution()
    assert solution.check_if_pangram(sentence="thequickbrownfoxjumpsoverthelazydog")
    assert not solution.check_if_pangram(sentence="leetcode")
