#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1854. Maximum Population Year
URL: https://leetcode.com/problems/maximum-population-year/description/
"""
from itertools import accumulate
from typing import List


class Solution:
    def maximum_population(self, logs: List[List[int]]) -> int:
        years: List[int] = [0] * 101
        for person in logs:
            years[person[0] - 1950] += 1
            years[person[1] - 1950] -= 1
        return max(range(len(years)), key=list(accumulate(years)).__getitem__) + 1950


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximum_population(logs=[[1993, 1999], [2000, 2010]]) == 1993
    assert (
        solution.maximum_population(logs=[[1950, 1961], [1960, 1971], [1970, 1981]])
        == 1960
    )
