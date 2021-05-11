#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1838. Frequency of the Most Frequent Element
URL: https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
"""

from typing import List


class Solution:
    def max_frequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        freq = 1
        left = 0
        window_cost = 0
        for right in range(1, len(nums)):
            window_cost += (right - left) * (nums[right] - nums[right - 1])
            while window_cost > k:
                window_cost -= nums[right] - nums[left]
                left += 1
            freq = max(freq, right - left + 1)
        return freq


if __name__ == "__main__":
    solution = Solution()
    assert solution.max_frequency(nums=[1, 2, 4], k=5) == 3
    assert solution.max_frequency(nums=[1, 4, 8, 13], k=5) == 2
    assert solution.max_frequency(nums=[3, 9, 6], k=2) == 1
