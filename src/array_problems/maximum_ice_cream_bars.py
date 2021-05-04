#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1833. Maximum Ice Cream Bars
URL: https://leetcode.com/problems/maximum-ice-cream-bars/description/
"""
from itertools import accumulate
from typing import List


# O(NlogN) / O(N)
class Solution:
    def max_ice_cream(self, costs: List[int], coins: int) -> int:
        return len(list(filter(lambda c: c <= coins, accumulate(sorted(costs)))))


# O(NlogN) / O(1)
# class Solution:
#     def max_ice_cream(self, costs: List[int], coins: int) -> int:
# costs.sort()
# for idx, cost in enumerate(costs):
#     coins -= cost
#     if coins < 0:
#         return idx
# return len(costs)


if __name__ == "__main__":
    solution = Solution()
    assert solution.max_ice_cream(costs=[1, 3, 2, 4, 1], coins=7) == 4
    assert solution.max_ice_cream(costs=[10, 6, 8, 7, 7, 8], coins=5) == 0
    assert solution.max_ice_cream(costs=[1, 6, 3, 1, 2, 5], coins=20) == 6
