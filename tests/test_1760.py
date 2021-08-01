#!/usr/bin/env python

import pytest

"""
Test 1760. Minimum Limit of Balls in a Bag
"""


@pytest.fixture(scope="session")
def init_variables_1760():
    from src.leetcode_1760_minimum_limit_of_balls_in_a_bag import Solution

    solution = Solution()

    def _init_variables_1760():
        return solution

    yield _init_variables_1760


class TestClass1760:
    def test_solution_0(self, init_variables_1760):
        assert init_variables_1760().minimumSize([9], 2) == 3

    def test_solution_1(self, init_variables_1760):
        assert init_variables_1760().minimumSize([2, 4, 8, 2], 4) == 2

    def test_solution_2(self, init_variables_1760):
        assert init_variables_1760().minimumSize([7, 17], 2) == 7
