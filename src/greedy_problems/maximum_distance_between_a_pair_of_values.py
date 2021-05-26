#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1855. Maximum Distance Between a Pair of Values
URL: https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/
"""

from typing import List


class Solution:
    def max_distance(self, nums1: List[int], nums2: List[int]) -> int:
        ret = i = j = 0
        while j < len(nums2) and i < len(nums1):
            if nums1[i] <= nums2[j]:
                ret = max(ret, j - i)
            else:
                i += 1
            j += 1
        return ret


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.max_distance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]) == 2
    )
    assert solution.max_distance(nums1=[2, 2, 2], nums2=[10, 10, 1]) == 1
    assert solution.max_distance(nums1=[30, 29, 19, 5], nums2=[25, 25, 25, 25, 25]) == 2
    assert solution.max_distance(nums1=[5, 4], nums2=[3, 2]) == 0
