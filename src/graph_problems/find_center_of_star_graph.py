#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1791. Find Center of Star Graph
URL: https://leetcode.com/problems/find-center-of-star-graph/description/
"""
from typing import List


class Solution:
    def find_center(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()


if __name__ == "__main__":
    solution = Solution()
    assert solution.find_center(edges=[[1, 2], [2, 3], [4, 2]]) == 2
    assert solution.find_center(edges=[[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
