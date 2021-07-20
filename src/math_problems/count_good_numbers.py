#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1922. Count Good Numbers
URL: https://leetcode.com/problems/count-good-numbers/description/
"""


class Solution:
    def count_good_numbers(self, n: int) -> int:
        exp, r = divmod(n, 2)
        res, base, mod = 1, 20, 10 ** 9 + 7
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % mod
            exp >>= 1
            base = (base * base) % mod
        return (res * (5 ** r)) % mod


if __name__ == "__main__":
    solution = Solution()
    assert solution.count_good_numbers(n=1) == 5
    assert solution.count_good_numbers(n=4) == 400
    assert solution.count_good_numbers(n=50) == 564908303
