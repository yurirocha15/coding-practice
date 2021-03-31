#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1793. Maximum Score of a Good Subarray
URL: https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/
"""
from typing import List


class Solution:
    def maximum_score(self, nums: List[int], k: int) -> int:
        i, j, n = k, k, len(nums)
        result = minimum = nums[k]

        while i > 0 or j < n - 1:
            if (nums[i - 1] if i > 0 else 0) > (nums[j + 1] if j < n - 1 else 0):
                i -= 1
            else:
                j += 1

            minimum = min(minimum, nums[i], nums[j])
            result = max(result, minimum * (j - i + 1))

        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.maximum_score(nums=[1, 4, 3, 7, 4, 5], k=3) == 15
    assert solution.maximum_score(nums=[5, 5, 4, 5, 4, 1, 1, 1], k=0) == 20
