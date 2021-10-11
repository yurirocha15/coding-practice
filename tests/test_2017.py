#!/usr/bin/env python

import pytest

"""
Test 2017. Grid Game
"""


@pytest.fixture(scope="session")
def init_variables_2017():
    from src.leetcode_2017_grid_game import Solution

    solution = Solution()

    def _init_variables_2017():
        return solution

    yield _init_variables_2017


class TestClass2017:
    def test_solution_0(self, init_variables_2017):
        assert init_variables_2017().gridGame([[2, 5, 4], [1, 5, 1]]) == 4

    def test_solution_1(self, init_variables_2017):
        assert init_variables_2017().gridGame([[3, 3, 1], [8, 5, 2]]) == 4

    def test_solution_2(self, init_variables_2017):
        assert init_variables_2017().gridGame([[1, 3, 1, 15], [1, 3, 3, 1]]) == 7
