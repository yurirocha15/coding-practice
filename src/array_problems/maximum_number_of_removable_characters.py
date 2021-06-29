#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1898. Maximum Number of Removable Characters
URL: https://leetcode.com/problems/maximum-number-of-removable-characters/description/
"""
from typing import List, Set


class Solution:
    def maximum_removals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(k: int) -> bool:
            p_idx = s_idx = 0
            unavailable: Set[int] = set(removable[:k])
            while s_idx < len(s):
                if s_idx in unavailable:
                    s_idx += 1
                    continue
                if p[p_idx] == s[s_idx]:
                    p_idx += 1
                if p_idx == len(p):
                    return True
                s_idx += 1
            return False

        left = 0
        right = len(removable)

        while left < right:
            middle = (left + right) // 2
            if is_subsequence(middle + 1):
                left = middle + 1
            else:
                right = middle

        return left


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximum_removals(s="abcacb", p="ab", removable=[3, 1, 0]) == 2
    assert (
        solution.maximum_removals(s="abcbddddd", p="abcd", removable=[3, 2, 1, 4, 5, 6])
        == 1
    )
    assert solution.maximum_removals(s="abcab", p="abc", removable=[0, 1, 2, 3, 4]) == 0
