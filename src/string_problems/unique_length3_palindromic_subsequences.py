#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1930. Unique Length-3 Palindromic Subsequences
URL: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
"""
import string


class Solution:
    def count_palindromic_subsequence(self, s: str) -> int:
        cnt = 0
        outer_index = {c: [-1, -1] for c in string.ascii_lowercase}
        for i, c in enumerate(s):
            if outer_index[c][0] == -1 or i < outer_index[c][0]:
                outer_index[c][0] = i
            elif i > outer_index[c][1]:
                outer_index[c][1] = i

        for idx in outer_index.values():
            if idx[0] != -1 and idx[1] != -1:
                cnt += len(set(s[idx[0] + 1 : idx[1]]))
        return cnt


if __name__ == "__main__":
    solution = Solution()
    assert solution.count_palindromic_subsequence(s="aabca") == 3
    assert solution.count_palindromic_subsequence(s="adc") == 0
    assert solution.count_palindromic_subsequence(s="bbcbaba") == 4
