#!/usr/bin/env python

import pytest

"""
Test 2033. Minimum Operations to Make a Uni-Value Grid
"""


@pytest.fixture(scope="session")
def init_variables_2033():
    from src.leetcode_2033_minimum_operations_to_make_a_uni_value_grid import Solution

    solution = Solution()

    def _init_variables_2033():
        return solution

    yield _init_variables_2033


class TestClass2033:
    def test_solution_0(self, init_variables_2033):
        assert init_variables_2033().minOperations([[2, 4], [6, 8]], 2) == 4

    def test_solution_1(self, init_variables_2033):
        assert init_variables_2033().minOperations([[1, 5], [2, 3]], 1) == 5

    def test_solution_2(self, init_variables_2033):
        assert init_variables_2033().minOperations([[1, 2], [3, 4]], 2) == -1
