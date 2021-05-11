#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1837. Sum of Digits in Base K
URL: https://leetcode.com/problems/sum-of-digits-in-base-k/description/
"""


class Solution:
    def sum_base(self, n: int, k: int) -> int:
        ret = 0
        while n >= k:
            ret += n % k
            n = n // k
        return ret + n

        # one-liner
        # return n if n < k else n % k + self.sumBase(n // k, k)


if __name__ == "__main__":
    solution = Solution()
    assert solution.sum_base(n=34, k=6) == 9
    assert solution.sum_base(n=10, k=10) == 1
