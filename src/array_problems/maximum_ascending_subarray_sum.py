#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1800. Maximum Ascending Subarray Sum
URL: https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
"""
from typing import List


class Solution:
    def max_ascending_sum(self, nums: List[int]) -> int:
        ret = cur_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            ret = max(ret, cur_sum)
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert solution.max_ascending_sum(nums=[10, 20, 30, 5, 10, 50]) == 65
    assert solution.max_ascending_sum(nums=[10, 20, 30, 40, 50]) == 150
    assert solution.max_ascending_sum(nums=[12, 17, 15, 13, 10, 11, 12]) == 33
    assert solution.max_ascending_sum(nums=[100, 10, 1]) == 100
