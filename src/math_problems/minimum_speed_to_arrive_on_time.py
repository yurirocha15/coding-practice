#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1870. Minimum Speed to Arrive on Time
URL: https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/
"""
from math import ceil
from typing import List


class Solution:
    def min_speed_on_time(self, dist: List[int], hour: float) -> int:
        if hour <= (len(dist) - 1):
            return -1
        left = 1
        right = 10 ** 7

        def check_valid(speed: int) -> bool:
            cur_time: float = 0.0
            for d in dist:
                cur_time = (d / speed) + ceil(cur_time)
                if cur_time > hour:
                    return False
            return True

        while left < right:
            med = (left + right) // 2
            valid = check_valid(med)
            if valid:
                right = med
            else:
                left = med + 1
        return right


if __name__ == "__main__":
    solution = Solution()
    assert solution.min_speed_on_time(dist=[1, 3, 2], hour=6) == 1
    assert solution.min_speed_on_time(dist=[1, 3, 2], hour=2.7) == 3
    assert solution.min_speed_on_time(dist=[1, 3, 2], hour=1.9) == -1
