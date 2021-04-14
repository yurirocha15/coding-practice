#!/usr/bin/env python
"""
Platform: LeetCode
Problem: 1808. Maximize Number of Nice Divisors
URL: https://leetcode.com/problems/maximize-number-of-nice-divisors/description/
"""


class Solution:
    def max_nice_divisors(self, primeFactors: int) -> int:
        quo: int = primeFactors // 3
        ret: int = primeFactors % 3
        modulo: int = 1000000007

        if quo == 0:
            return ret
        if ret == 0:
            return pow(3, quo, modulo) % modulo
        if ret == 1:
            return 4 * pow(3, quo - 1, modulo) % modulo
        return 2 * pow(3, quo, modulo) % modulo


if __name__ == "__main__":
    solution = Solution()
    assert solution.max_nice_divisors(primeFactors=5) == 6
    assert solution.max_nice_divisors(primeFactors=8) == 18
