#!/usr/bin/env python

import pytest

"""
Test 1835. Find XOR Sum of All Pairs Bitwise AND
"""


@pytest.fixture(scope="session")
def init_variables_1835():
    from src.leetcode_1835_find_xor_sum_of_all_pairs_bitwise_and import Solution

    solution = Solution()

    def _init_variables_1835():
        return solution

    yield _init_variables_1835


class TestClass1835:
    def test_solution_0(self, init_variables_1835):
        assert init_variables_1835().getXORSum([1, 2, 3], [6, 5]) == 0

    def test_solution_1(self, init_variables_1835):
        assert init_variables_1835().getXORSum([12], [4]) == 4
