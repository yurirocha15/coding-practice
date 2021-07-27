#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1931. Painting a Grid With Three Different Colors
URL: https://leetcode.com/problems/painting-a-grid-with-three-different-colors/description/
"""
from functools import lru_cache


class Solution:
    def color_the_grid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7

        @lru_cache(None)
        def dp(index: int, row: int):
            if index == (m * n):
                return 1
            c, r = divmod(index, m)

            colors = set([0b00, 0b01, 0b10])  # r g b
            if r > 0:
                colors.discard(row & 0b11)
            if c > 0:
                colors.discard((row >> 2 * (m - 1)) & 0b11)

            ret = 0
            for color in colors:
                ret += dp(index + 1, ((row << 2) | color) & ((1 << (2 * m)) - 1))
            return ret % mod

        ret = dp(0, (1 << (2 * m)) - 1) % mod
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.color_the_grid(m=1, n=1) == 3
    assert solution.color_the_grid(m=1, n=2) == 6
    assert solution.color_the_grid(m=5, n=5) == 580986
