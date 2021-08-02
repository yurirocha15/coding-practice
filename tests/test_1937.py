#!/usr/bin/env python

import pytest

"""
Test 1937. Maximum Number of Points with Cost
"""


@pytest.fixture(scope="session")
def init_variables_1937():
    from src.leetcode_1937_maximum_number_of_points_with_cost import Solution

    solution = Solution()

    def _init_variables_1937():
        return solution

    yield _init_variables_1937


class TestClass1937:
    def test_solution_0(self, init_variables_1937):
        assert init_variables_1937().maxPoints([[1, 2, 3], [1, 5, 1], [3, 1, 1]]) == 9

    def test_solution_1(self, init_variables_1937):
        assert init_variables_1937().maxPoints([[1, 5], [2, 3], [4, 2]]) == 11
