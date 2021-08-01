# @l2g 1931 python3
# [1931] Painting a Grid With Three Different Colors
# Difficulty: Hard
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors
#
# You are given two integers m and n.Consider an m x n grid where each cell is initially white.
# You can paint each cell red,green,or blue.All cells must be painted.
# Return the number of ways to color the grid with no two adjacent cells having the same color.
# Since the answer can be very large,return it modulo 10^9 + 7.
#
# Example 1:
#
#
# Input: m = 1, n = 1
# Output: 3
# Explanation: The three possible colorings are shown in the image above.
#
# Example 2:
#
#
# Input: m = 1, n = 2
# Output: 6
# Explanation: The six possible colorings are shown in the image above.
#
# Example 3:
#
# Input: m = 5, n = 5
# Output: 580986
#
#
# Constraints:
#
# 1 <= m <= 5
# 1 <= n <= 1000
#
#


# @l2g 1931 python3
# [1931] Painting a Grid With Three Different Colors
# Difficulty: Hard
# https://leetcode.com/problems/painting-a-grid-with-three-different-colors
#
# You are given two integers m and n.Consider an m x n grid where each cell is initially white.
# You can paint each cell red,green,or blue.All cells must be painted.
# Return the number of ways to color the grid with no two adjacent cells having the same color.
# Since the answer can be very large,return it modulo 10^9 + 7.
#
# Example 1:
#
#
# Input: m = 1, n = 1
# Output: 3
# Explanation: The three possible colorings are shown in the image above.
#
# Example 2:
#
#
# Input: m = 1, n = 2
# Output: 6
# Explanation: The six possible colorings are shown in the image above.
#
# Example 3:
#
# Input: m = 5, n = 5
# Output: 580986
#
#
# Constraints:
#
# 1 <= m <= 5
# 1 <= n <= 1000
#
#


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
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
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1931.py")])
