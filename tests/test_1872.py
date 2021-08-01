#!/usr/bin/env python

import pytest

"""
Test 1872. Stone Game VIII
"""


@pytest.fixture(scope="session")
def init_variables_1872():
    from src.leetcode_1872_stone_game_viii import Solution

    solution = Solution()

    def _init_variables_1872():
        return solution

    yield _init_variables_1872


class TestClass1872:
    def test_solution_0(self, init_variables_1872):
        assert init_variables_1872().stoneGameVIII([-1, 2, -3, 4, -5]) == 5

    def test_solution_1(self, init_variables_1872):
        assert init_variables_1872().stoneGameVIII([7, -6, 5, 10, 5, -2, -6]) == 13

    def test_solution_2(self, init_variables_1872):
        assert init_variables_1872().stoneGameVIII([-10, -12]) == -22
