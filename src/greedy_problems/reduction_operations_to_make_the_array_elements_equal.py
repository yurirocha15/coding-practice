#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1887. Reduction Operations to Make the Array Elements Equal
URL: https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/
"""
from collections import Counter
from itertools import accumulate
from typing import List


class Solution:
    def reduction_operations(self, nums: List[int]) -> int:
        return sum(accumulate((n[1] for n in sorted(Counter(nums).items())[-1:0:-1])))


if __name__ == "__main__":
    solution = Solution()
    assert solution.reduction_operations(nums=[5, 1, 3]) == 3
    assert solution.reduction_operations(nums=[1, 1, 1]) == 0
    assert solution.reduction_operations(nums=[1, 1, 2, 2, 3]) == 4
