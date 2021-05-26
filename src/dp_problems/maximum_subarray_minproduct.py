#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1856. Maximum Subarray Min-Product
URL: https://leetcode.com/problems/maximum-subarray-min-product/description/
"""
from collections import deque
from itertools import accumulate
from typing import Deque, List


class Solution:
    def max_sum_min_product(self, nums: List[int]) -> int:
        pre_sum = [0] + list(accumulate(nums))
        dq: Deque[int] = deque()
        res = 0
        for i in range(len(nums) + 1):
            while dq and (i == len(nums) or nums[dq[-1]] > nums[i]):
                j = dq.pop()
                res = max(
                    res, nums[j] * (pre_sum[i] - pre_sum[dq[-1] + 1 if dq else 0])
                )
            dq.append(i)
        return res % (10 ** 9 + 7)


if __name__ == "__main__":
    solution = Solution()
    assert solution.max_sum_min_product(nums=[1, 2, 3, 2]) == 14
    assert solution.max_sum_min_product(nums=[1, 10, 10, 9, 10]) == 351
    assert solution.max_sum_min_product(nums=[2, 3, 3, 1, 2]) == 18
    assert solution.max_sum_min_product(nums=[3, 1, 5, 6, 4, 2]) == 60
