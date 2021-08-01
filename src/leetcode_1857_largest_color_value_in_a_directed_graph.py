# @l2g 1857 python3
# [1857] Largest Color Value in a Directed Graph
# Difficulty: Hard
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph
#
# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.
# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed).
# You are also given a 2D array edges where edges[j] = [aj,
# bj] indicates that there is a directed edge from node aj to node bj.
# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ...
# -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k.
# The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.
# Return the largest color value of any valid path in the given graph,
# or -1 if the graph contains a cycle.
#
# Example 1:
#
#
# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
#
# Example 2:
#
#
# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
#
#
# Constraints:
#
# n == colors.length
# m == edges.length
# 1 <= n <= 10^5
# 0 <= m <= 10^5
# colors consists of lowercase English letters.
# 0 <= aj, bj < n
#

from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
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
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1857.py")])
