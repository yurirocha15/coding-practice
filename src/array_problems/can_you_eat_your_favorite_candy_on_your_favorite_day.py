#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1744. Can You Eat Your Favorite Candy on Your Favorite Day?
URL: https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/description/
"""
from typing import List


class Solution:
    def can_eat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        pre_sum = [0]
        for cnt in candiesCount:
            pre_sum.append(pre_sum[-1] + cnt)
        ret: List[bool] = []
        for query in queries:
            end = pre_sum[query[0] + 1]
            start = pre_sum[query[0]] // query[2]
            if start <= query[1] < end:
                ret.append(True)
            else:
                ret.append(False)
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.can_eat(
        [7, 4, 5, 3, 8], [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]
    ) == [True, False, True]
    assert solution.can_eat(
        [5, 2, 6, 4, 1], [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]
    ) == [False, True, True, False, False]
