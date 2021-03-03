#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1759. Count Number of Homogenous Substrings
URL: https://leetcode.com/problems/count-number-of-homogenous-substrings/description/
"""
# O(N)/O(1)


class Solution:
    def count_homogenous(self, s: str) -> int:
        ret = last_idx = 0
        for i, c in enumerate(s):
            if c != s[last_idx]:
                ret += ((i - last_idx) + 1) * (i - last_idx) // 2  # Gauss formula
                last_idx = i
        ret += ((len(s) - last_idx) + 1) * (len(s) - last_idx) // 2
        return ret % 1000000007


if __name__ == "__main__":
    solution = Solution()
    assert solution.count_homogenous(s="abbcccaa") == 13
    assert solution.count_homogenous(s="xy") == 2
    assert solution.count_homogenous(s="zzzzz") == 15
