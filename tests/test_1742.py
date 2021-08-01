#!/usr/bin/env python

import pytest

"""
Test 1742. Maximum Number of Balls in a Box
"""


@pytest.fixture(scope="session")
def init_variables_1742():
    from src.leetcode_1742_maximum_number_of_balls_in_a_box import Solution

    solution = Solution()

    def _init_variables_1742():
        return solution

    yield _init_variables_1742


class TestClass1742:
    def test_solution_0(self, init_variables_1742):
        assert init_variables_1742().countBalls(1, 10) == 2

    def test_solution_1(self, init_variables_1742):
        assert init_variables_1742().countBalls(5, 15) == 2

    def test_solution_2(self, init_variables_1742):
        assert init_variables_1742().countBalls(19, 28) == 2
