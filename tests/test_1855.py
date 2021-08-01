#!/usr/bin/env python

import pytest

"""
Test 1855. Maximum Distance Between a Pair of Values
"""


@pytest.fixture(scope="session")
def init_variables_1855():
    from src.leetcode_1855_maximum_distance_between_a_pair_of_values import Solution

    solution = Solution()

    def _init_variables_1855():
        return solution

    yield _init_variables_1855


class TestClass1855:
    def test_solution_0(self, init_variables_1855):
        assert (
            init_variables_1855().maxDistance([55, 30, 5, 4, 2], [100, 20, 10, 10, 5])
            == 2
        )

    def test_solution_1(self, init_variables_1855):
        assert init_variables_1855().maxDistance([2, 2, 2], [10, 10, 1]) == 1

    def test_solution_2(self, init_variables_1855):
        assert (
            init_variables_1855().maxDistance([30, 29, 19, 5], [25, 25, 25, 25, 25])
            == 2
        )

    def test_solution_3(self, init_variables_1855):
        assert init_variables_1855().maxDistance([5, 4], [3, 2]) == 0
