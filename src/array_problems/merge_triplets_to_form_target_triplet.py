#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1899. Merge Triplets to Form Target Triplet
URL: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/
"""

from typing import List


class Solution:
    def merge_triplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res: List[bool] = [False] * 3
        for triplet in triplets:
            if all(n <= t for n, t in zip(triplet, target)):
                res = [r or (n == t) for r, n, t in zip(res, triplet, target)]
        return all(res)


if __name__ == "__main__":
    solution = Solution()
    assert solution.merge_triplets(
        triplets=[[2, 5, 3], [1, 8, 4], [1, 7, 5]], target=[2, 7, 5]
    )
    assert solution.merge_triplets(triplets=[[1, 3, 4], [2, 5, 8]], target=[2, 5, 8])
    assert solution.merge_triplets(
        triplets=[[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], target=[5, 5, 5]
    )
    assert not solution.merge_triplets(
        triplets=[[3, 4, 5], [4, 5, 6]], target=[3, 2, 5]
    )
