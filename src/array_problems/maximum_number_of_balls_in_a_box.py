#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1742. Maximum Number of Balls in a Box
URL: https://leetcode.com/problems/maximum-number-of-balls-in-a-box/description/
"""
from collections import defaultdict
from typing import DefaultDict


class Solution:
    def sum_digits(self, n: int) -> int:
        ret = 0
        while n:
            ret, n = ret + n % 10, n // 10
        return ret

    def count_balls(self, lowLimit: int, highLimit: int) -> int:
        cnt: DefaultDict[int, int] = defaultdict(lambda: 0)
        for i in range(lowLimit, highLimit + 1):
            cnt[self.sum_digits(i)] += 1
        return max(cnt.values())


if __name__ == "__main__":
    solution = Solution()
    assert solution.count_balls(lowLimit=1, highLimit=10) == 2
    assert solution.count_balls(lowLimit=5, highLimit=15) == 2
    assert solution.count_balls(lowLimit=19, highLimit=28) == 2
