#!/usr/bin/env python

import pytest

"""
Test 1769. Minimum Number of Operations to Move All Balls to Each Box
"""


@pytest.fixture(scope="session")
def init_variables_1769():
    from src.leetcode_1769_minimum_number_of_operations_to_move_all_balls_to_each_box import Solution

    solution = Solution()

    def _init_variables_1769():
        return solution

    yield _init_variables_1769


class TestClass1769:
    def test_solution_0(self, init_variables_1769):
        assert init_variables_1769().minOperations("110") == [1, 1, 3]

    def test_solution_1(self, init_variables_1769):
        assert init_variables_1769().minOperations("001011") == [11, 8, 5, 4, 3, 4]
