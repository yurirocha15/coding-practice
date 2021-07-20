#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1921. Eliminate Maximum Number of Monsters
URL: https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/
"""

from typing import List


class Solution:
    def eliminate_maximum(self, dist: List[int], speed: List[int]) -> int:
        arrive_time: List[int] = sorted([-(s // -d) for s, d in zip(dist, speed)])
        for i in range(len(arrive_time)):
            if i >= arrive_time[i]:
                return i
        return len(arrive_time)


if __name__ == "__main__":
    solution = Solution()
    assert solution.eliminate_maximum(dist=[1, 3, 4], speed=[1, 1, 1]) == 3
    assert solution.eliminate_maximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]) == 1
    assert solution.eliminate_maximum(dist=[3, 2, 4], speed=[5, 3, 2]) == 1
