#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1760. Minimum Limit of Balls in a Bag
URL: https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/
"""
from typing import List


class Solution:
    # return the minimum number of operations
    # to make every number smaller or equal than cost
    def get_min_operation(self, nums: List[int], cost: int) -> int:
        ret: int = 0
        for n in nums:
            # if n is divisible by the cost, it takes one less operation
            ret += (n // cost) - int((n % cost) == 0)
        return ret

    def minimum_size(self, nums: List[int], maxOperations: int) -> int:
        start, end = 1, max(nums)  # min and maximum cost possible
        ret: int = end
        # binary search
        while start < end:
            mid = (start + end) // 2
            if self.get_min_operation(nums, mid) <= maxOperations:
                end = ret = mid
            else:
                start = (mid) + 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.minimum_size(nums=[9], maxOperations=2) == 3
    assert solution.minimum_size(nums=[2, 4, 8, 2], maxOperations=4) == 2
    assert solution.minimum_size(nums=[7, 17], maxOperations=2) == 7
