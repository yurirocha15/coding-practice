#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1768. Merge Strings Alternately
URL: https://leetcode.com/problems/merge-strings-alternately/description/
"""


class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        small_len = min(len(word1), len(word2))
        return (
            "".join(map(lambda a, b: a + b, word1[:small_len], word2[:small_len]))
            + word1[small_len:]
            + word2[small_len:]
        )


if __name__ == "__main__":
    solution = Solution()
    assert solution.merge_alternately(word1="abc", word2="pqr") == "apbqcr"
    assert solution.merge_alternately(word1="ab", word2="pqrs") == "apbqrs"
    assert solution.merge_alternately(word1="abcd", word2="pq") == "apbqcd"
