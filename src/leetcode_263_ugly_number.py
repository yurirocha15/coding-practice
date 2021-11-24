# @l2g 263 python3
# [263] Ugly Number
# Difficulty: Easy
# https://leetcode.com/problems/ugly-number
#
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.
#
# Example 1:
#
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:
#
# Input: n = 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
#
# Example 3:
#
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
#
# Example 4:
#
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
#
#
# Constraints:
#
# -2^31 <= n <= 2^31 - 1
#
#


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        primes = [2, 3, 5]
        idx = 0
        while idx < 3:
            if n % primes[idx] == 0:
                n //= primes[idx]
            else:
                idx += 1
        return n == 1


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_263.py")])
