# @l2g 1808 python3
# [1808] Maximize Number of Nice Divisors
# Difficulty: Hard
# https://leetcode.com/problems/maximize-number-of-nice-divisors
#
# You are given a positive integer primeFactors.
# You are asked to construct a positive integer n that satisfies the following conditions:
#
# The number of prime factors of n (not necessarily distinct) is at most primeFactors.
# The number of nice divisors of n is maximized.
# Note that a divisor of n is nice if it is divisible by every prime factor of n.For example,
# if n = 12,then its prime factors are [2,2,3],then 6 and 12 are nice divisors,while 3 and 4 are not.
#
# Return the number of nice divisors of n.Since that number can be too large,
# return it modulo 10^9 + 7.
# Note that a prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
# The prime factors of a number n is a list of prime numbers such that their product equals n.
#
# Example 1:
#
# Input: primeFactors = 5
# Output: 6
# Explanation: 200 is a valid value of n.
# It has 5 prime factors: [2,2,2,5,5], and it has 6 nice divisors: [10,20,40,50,100,200].
# There is not other value of n that has at most 5 prime factors and more nice divisors.
#
# Example 2:
#
# Input: primeFactors = 8
# Output: 18
#
#
# Constraints:
#
# 1 <= primeFactors <= 10^9
#


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        quo = primeFactors // 3
        ret = primeFactors % 3
        modulo = 1000000007

        if quo == 0:
            return ret
        if ret == 0:
            return pow(3, quo, modulo) % modulo
        if ret == 1:
            return 4 * pow(3, quo - 1, modulo) % modulo
        return 2 * pow(3, quo, modulo) % modulo


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.join("tests", "test_1808.py")])
