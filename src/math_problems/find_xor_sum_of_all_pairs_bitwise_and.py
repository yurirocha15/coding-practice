#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1835. Find XOR Sum of All Pairs Bitwise AND
URL: https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/description/
"""
from functools import reduce
from typing import List


class Solution:
    def get_x_o_r_sum(self, arr1: List[int], arr2: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, arr1) & reduce(lambda a, b: a ^ b, arr2)


if __name__ == "__main__":
    solution = Solution()
    assert solution.get_x_o_r_sum(arr1=[1, 2, 3], arr2=[6, 5]) == 0
    assert solution.get_x_o_r_sum(arr1=[12], arr2=[4]) == 4
