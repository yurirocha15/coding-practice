#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1761. Minimum Degree of a Connected Trio in a Graph
URL: https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/description/
"""
from collections import defaultdict
from typing import DefaultDict, List, Set


class Solution:
    def min_trio_degree(self, n: int, edges: List[List[int]]) -> int:
        # create graph
        graph: DefaultDict[int, Set[int]] = defaultdict(set)
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])

        ret: int = -1
        # pre-calculate lengths
        graph_len = {n: len(graph[n]) for n in graph.keys()}

        for a in graph.keys():
            for b in graph[a]:
                # using set intersection
                for c in graph[b] & graph[a]:
                    degree = graph_len[a] + graph_len[b] + graph_len[c] - 6
                    ret = degree if ret == -1 else min(ret, degree)
                # we already checked every triangle with a and b, so dont need to check again
                graph[b].discard(a)

        return ret


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.min_trio_degree(
            n=6, edges=[[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]
        )
        == 3
    )
    assert (
        solution.min_trio_degree(
            n=7, edges=[[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]
        )
        == 0
    )
