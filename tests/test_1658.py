#!/usr/bin/env python

import pytest

"""
Test 1658. Minimum Operations to Reduce X to Zero
"""


@pytest.fixture(scope="session")
def init_variables_1658():
    from src.leetcode_1658_minimum_operations_to_reduce_x_to_zero import Solution

    solution = Solution()

    def _init_variables_1658():
        return solution

    yield _init_variables_1658


class TestClass1658:
    def test_solution_0(self, init_variables_1658):
        assert init_variables_1658().minOperations([1, 1, 4, 2, 3], 5) == 2

    def test_solution_1(self, init_variables_1658):
        assert init_variables_1658().minOperations([5, 6, 7, 8, 9], 4) == -1

    def test_solution_2(self, init_variables_1658):
        assert init_variables_1658().minOperations([3, 2, 20, 1, 1, 3], 10) == 5
