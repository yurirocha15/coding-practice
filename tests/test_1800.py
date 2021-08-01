#!/usr/bin/env python

import pytest

"""
Test 1800. Maximum Ascending Subarray Sum
"""


@pytest.fixture(scope="session")
def init_variables_1800():
    from src.leetcode_1800_maximum_ascending_subarray_sum import Solution

    solution = Solution()

    def _init_variables_1800():
        return solution

    yield _init_variables_1800


class TestClass1800:
    def test_solution_0(self, init_variables_1800):
        assert init_variables_1800().maxAscendingSum([10, 20, 30, 5, 10, 50]) == 65

    def test_solution_1(self, init_variables_1800):
        assert init_variables_1800().maxAscendingSum([10, 20, 30, 40, 50]) == 150

    def test_solution_2(self, init_variables_1800):
        assert init_variables_1800().maxAscendingSum([12, 17, 15, 13, 10, 11, 12]) == 33

    def test_solution_3(self, init_variables_1800):
        assert init_variables_1800().maxAscendingSum([100, 10, 1]) == 100
