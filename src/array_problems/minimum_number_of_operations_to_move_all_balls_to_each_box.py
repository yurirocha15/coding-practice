#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1769. Minimum Number of Operations to Move All Balls to Each Box
URL: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
"""
from typing import List


class Solution:
    def min_operations(self, boxes: str) -> List[int]:
        ret = [0] * len(boxes)
        cur_cost = [0, 0]
        for i, b in enumerate(boxes):
            cur_cost[0] += cur_cost[1]
            ret[i] += cur_cost[0]
            if b == "1":
                cur_cost[1] += 1
        cur_cost = [0, 0]
        for i, b in reversed(list(enumerate(boxes))):
            cur_cost[0] += cur_cost[1]
            ret[i] += cur_cost[0]
            if b == "1":
                cur_cost[1] += 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.min_operations(boxes="110") == [1, 1, 3]
    assert solution.min_operations(boxes="001011") == [11, 8, 5, 4, 3, 4]
