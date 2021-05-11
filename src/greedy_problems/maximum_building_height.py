#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1840. Maximum Building Height
URL: https://leetcode.com/problems/maximum-building-height/description/
"""

from typing import List

# First try TLE
# class Solution:
#     def max_building(self, n: int, restrictions: List[List[int]]) -> int:
#         height: List[int] = [10**9] * (n + 1)
#         for r in restrictions:
#             height[r[0]] = r[1]
#         curr_height = 0
#         height[0] = height[1] = 0
#         for idx in range(2, n + 1):
#             curr_height = height[idx] = min(curr_height + 1, height[idx])
#         max_height = curr_height = height[-1]
#         for idx in range(n - 1, 1, -1):
#             curr_height = height[idx] = min(height[idx], curr_height + 1)
#             max_height = max(max_height, height[idx])
#         return max_height


class Solution:
    def max_building(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.extend([[1, 0], [n, n - 1]])
        restrictions.sort()
        for i in range(1, len(restrictions)):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i][0] - restrictions[i - 1][0] + restrictions[i - 1][1],
            )
        for i in range(len(restrictions) - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][0] - restrictions[i][0] + restrictions[i + 1][1],
            )
        max_height = 0
        for i in range(1, len(restrictions)):
            max_height = max(
                max_height,
                (
                    restrictions[i][1]
                    + restrictions[i - 1][1]
                    + restrictions[i][0]
                    - restrictions[i - 1][0]
                )
                // 2,
            )
        return max_height


if __name__ == "__main__":
    solution = Solution()
    assert solution.max_building(n=5, restrictions=[[2, 1], [4, 1]]) == 2
    assert solution.max_building(n=6, restrictions=[]) == 5
    assert (
        solution.max_building(n=10, restrictions=[[5, 3], [2, 5], [7, 4], [10, 3]]) == 5
    )
