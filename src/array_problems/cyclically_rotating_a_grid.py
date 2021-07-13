#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1914. Cyclically Rotating a Grid
URL: https://leetcode.com/problems/cyclically-rotating-a-grid/description/
"""

from typing import List


class Solution:
    def rotate_grid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        x, y = 0, 0
        h, w = len(grid), len(grid[0])
        for _ in range(min(h, w) // 2):
            tmp: List[int] = (
                [grid[i][y] for i in range(x, x + h)]  # left
                + [grid[x + h - 1][i] for i in range(y + 1, y + w)]  # bottom
                + [grid[i][y + w - 1] for i in range(x + h - 2, x - 1, -1)]  # right
                + [grid[x][i] for i in range(y + w - 2, y, -1)]  # top
            )
            total = len(tmp)
            offset = k % total
            tmp = tmp[-offset:] + tmp[:-offset]
            t_idx = 0
            for i in range(x, x + h):
                grid[i][y] = tmp[t_idx]
                t_idx += 1
            for i in range(y + 1, y + w):
                grid[x + h - 1][i] = tmp[t_idx]
                t_idx += 1
            for i in range(x + h - 2, x - 1, -1):
                grid[i][y + w - 1] = tmp[t_idx]
                t_idx += 1
            for i in range(y + w - 2, y, -1):
                grid[x][i] = tmp[t_idx]
                t_idx += 1
            x, y = x + 1, y + 1
            h, w = h - 2, w - 2
        return grid


if __name__ == "__main__":
    solution = Solution()
    assert solution.rotate_grid(grid=[[40, 10], [30, 20]], k=1) == [[10, 20], [40, 30]]
    assert solution.rotate_grid(
        grid=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], k=2
    ) == [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 9, 13, 14]]
