#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1886. Determine Whether Matrix Can Be Obtained By Rotation
URL: https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/description/
"""

from typing import List


class Solution:
    def find_rotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if target == mat:
                return True
            mat = [
                [mat[j][i] for j in range(len(mat))]
                for i in range(len(mat[0]) - 1, -1, -1)
            ]
        return False


if __name__ == "__main__":
    solution = Solution()
    assert solution.find_rotation(mat=[[0, 1], [1, 0]], target=[[1, 0], [0, 1]])
    assert not solution.find_rotation(mat=[[0, 1], [1, 1]], target=[[1, 0], [0, 1]])
    assert solution.find_rotation(
        mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]], target=[[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    )
