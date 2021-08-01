# @l2g 1914 python3
# [1914] Cyclically Rotating a Grid
# Difficulty: Medium
# https://leetcode.com/problems/cyclically-rotating-a-grid
#
# You are given an m x n integer matrix grid​​​,where m and n are both even integers,and an integer k.
# The matrix is composed of several layers,which is shown in the below image,
# where each color is its own layer:
#
# A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix.
# To cyclically rotate a layer once,
# each element in the layer will take the place of the adjacent element in the counter-clockwise direction.
# An example rotation is shown below:
#
# Return the matrix after applying k cyclic rotations to it.
#
# Example 1:
#
#
# Input: grid = [[40,10],[30,20]], k = 1
# Output: [[10,20],[40,30]]
# Explanation: The figures above represent the grid at every state.
#
# Example 2:
#
#
# Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
# Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
# Explanation: The figures above represent the grid at every state.
#
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 2 <= m, n <= 50
# Both m and n are even integers.
# 1 <= grid[i][j] <= 5000
# 1 <= k <= 10^9
#

from typing import List


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        x, y = 0, 0
        h, w = len(grid), len(grid[0])
        for _ in range(min(h, w) // 2):
            tmp: List[int] = (
                [grid[i][y] for i in range(x, x + h)]
                + [grid[x + h - 1][i] for i in range(y + 1, y + w)]
                + [grid[i][y + w - 1] for i in range(x + h - 2, x - 1, -1)]
                + [grid[x][i] for i in range(y + w - 2, y, -1)]
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
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1914.py")])
