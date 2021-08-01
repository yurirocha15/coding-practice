#!/usr/bin/env python

import pytest

"""
Test 1921. Eliminate Maximum Number of Monsters
"""


@pytest.fixture(scope="session")
def init_variables_1921():
    from src.leetcode_1921_eliminate_maximum_number_of_monsters import Solution

    solution = Solution()

    def _init_variables_1921():
        return solution

    yield _init_variables_1921


class TestClass1921:
    def test_solution_0(self, init_variables_1921):
        assert init_variables_1921().eliminateMaximum([1, 3, 4], [1, 1, 1]) == 3

    def test_solution_1(self, init_variables_1921):
        assert init_variables_1921().eliminateMaximum([1, 1, 2, 3], [1, 1, 1, 1]) == 1

    def test_solution_2(self, init_variables_1921):
        assert init_variables_1921().eliminateMaximum([3, 2, 4], [5, 3, 2]) == 1
