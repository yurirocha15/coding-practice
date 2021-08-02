#!/usr/bin/env python

import pytest

"""
Test 1936. Add Minimum Number of Rungs
"""


@pytest.fixture(scope="session")
def init_variables_1936():
    from src.leetcode_1936_add_minimum_number_of_rungs import Solution

    solution = Solution()

    def _init_variables_1936():
        return solution

    yield _init_variables_1936


class TestClass1936:
    def test_solution_0(self, init_variables_1936):
        assert init_variables_1936().addRungs([1, 3, 5, 10], 2) == 2

    def test_solution_1(self, init_variables_1936):
        assert init_variables_1936().addRungs([3, 6, 8, 10], 3) == 0

    def test_solution_2(self, init_variables_1936):
        assert init_variables_1936().addRungs([3, 4, 6, 7], 2) == 1

    def test_solution_3(self, init_variables_1936):
        assert init_variables_1936().addRungs([5], 10) == 0
