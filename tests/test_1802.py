#!/usr/bin/env python

import pytest

"""
Test 1802. Maximum Value at a Given Index in a Bounded Array
"""


@pytest.fixture(scope="session")
def init_variables_1802():
    from src.leetcode_1802_maximum_value_at_a_given_index_in_a_bounded_array import Solution

    solution = Solution()

    def _init_variables_1802():
        return solution

    yield _init_variables_1802


class TestClass1802:
    def test_solution_0(self, init_variables_1802):
        assert init_variables_1802().maxValue(4, 2, 6) == 2

    def test_solution_1(self, init_variables_1802):
        assert init_variables_1802().maxValue(6, 1, 10) == 3
