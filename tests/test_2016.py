#!/usr/bin/env python

import pytest

"""
Test 2016. Maximum Difference Between Increasing Elements
"""


@pytest.fixture(scope="session")
def init_variables_2016():
    from src.leetcode_2016_maximum_difference_between_increasing_elements import Solution

    solution = Solution()

    def _init_variables_2016():
        return solution

    yield _init_variables_2016


class TestClass2016:
    def test_solution_0(self, init_variables_2016):
        assert init_variables_2016().maximumDifference([7, 1, 5, 4]) == 4

    def test_solution_1(self, init_variables_2016):
        assert init_variables_2016().maximumDifference([9, 4, 3, 2]) == -1

    def test_solution_2(self, init_variables_2016):
        assert init_variables_2016().maximumDifference([1, 5, 2, 10]) == 9
