#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1792. Maximum Average Pass Ratio
URL: https://leetcode.com/problems/maximum-average-pass-ratio/description/
"""
import heapq
from typing import List, Tuple


class Solution:
    def max_average_ratio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq: List[Tuple[float, List[int]]] = [
            (c[0] / c[1] - (c[0] + 1) / (c[1] + 1), c) for c in classes
        ]
        heapq.heapify(pq)

        for _ in range(extraStudents):
            _, c = heapq.heappop(pq)
            c = [c[0] + 1, c[1] + 1]
            heapq.heappush(pq, ((c[0] / c[1] - (c[0] + 1) / (c[1] + 1), c)))

        return sum(map(lambda c: (c[1][0]) / (c[1][1]), pq)) / len(pq)


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.max_average_ratio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2)
        - 0.78333
        < 10e-5
    )
    assert (
        solution.max_average_ratio(
            classes=[[2, 4], [3, 9], [4, 5], [2, 10]], extraStudents=4
        )
        - 0.53485
        < 10e-5
    )
