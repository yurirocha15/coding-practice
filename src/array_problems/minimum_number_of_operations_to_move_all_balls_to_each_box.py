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
        cur_cost, num_balls = 0, 0
        cur_cost_2, num_balls_2 = 0, 0

        for idx, rev_idx in zip(range(len(boxes)), range(len(boxes) - 1, -1, -1)):
            cur_cost += num_balls
            cur_cost_2 += num_balls_2
            ret[idx] += cur_cost
            ret[rev_idx] += cur_cost_2
            if boxes[idx] == "1":
                num_balls += 1
            if boxes[rev_idx] == "1":
                num_balls_2 += 1

        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.min_operations(boxes="110") == [1, 1, 3]
    assert solution.min_operations(boxes="001011") == [11, 8, 5, 4, 3, 4]
