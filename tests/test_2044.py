#!/usr/bin/env python

import pytest

"""
Test 2044. Count Number of Maximum Bitwise-OR Subsets
"""


@pytest.fixture(scope="session")
def init_variables_2044():
    from src.leetcode_2044_count_number_of_maximum_bitwise_or_subsets import Solution

    solution = Solution()

    def _init_variables_2044():
        return solution

    yield _init_variables_2044


class TestClass2044:
    def test_solution_0(self, init_variables_2044):
        assert init_variables_2044().countMaxOrSubsets([3, 1]) == 2

    def test_solution_1(self, init_variables_2044):
        assert init_variables_2044().countMaxOrSubsets([2, 2, 2]) == 7

    def test_solution_2(self, init_variables_2044):
        assert init_variables_2044().countMaxOrSubsets([3, 2, 1, 5]) == 6

    def test_solution_2(self, init_variables_2044):
        assert (
            init_variables_2044().countMaxOrSubsets([84, 74, 92, 12, 37, 84, 41, 5, 63])
            == 324
        )
