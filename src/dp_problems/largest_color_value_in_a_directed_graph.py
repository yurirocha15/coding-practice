#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1857. Largest Color Value in a Directed Graph
URL: https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
"""
from typing import List


class Solution:
    def largest_path_value(self, colors: str, edges: List[List[int]]) -> int:
        adj_mat: List[List[int]] = [[] for _ in range(len(colors))]
        visited = [0] * len(colors)
        dp: List[List[int]] = [[0] * 26 for _ in range(len(colors))]
        for edge in edges:
            adj_mat[edge[0]].append(edge[1])

        def dfs(node: int) -> int:
            if not visited[node]:
                visited[node] = -1
                for child in adj_mat[node]:
                    if dfs(child) == -1:
                        return -1
                    for color in range(26):
                        dp[node][color] = max(dp[node][color], dp[child][color])
                dp[node][ord(colors[node]) - ord("a")] += 1
                visited[node] = 1
            return -1 if visited[node] == -1 else max(dp[node])

        ret = 0
        for node in range(len(colors)):
            val = dfs(node)
            if val == -1:
                return -1
            ret = max(ret, val)

        return ret


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.largest_path_value(
            colors="abaca", edges=[[0, 1], [0, 2], [2, 3], [3, 4]]
        )
        == 3
    )
    assert solution.largest_path_value(colors="a", edges=[[0, 0]]) == -1
