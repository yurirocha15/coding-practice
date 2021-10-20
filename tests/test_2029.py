#!/usr/bin/env python

import pytest

"""
Test 2029. Stone Game IX
"""


@pytest.fixture(scope="session")
def init_variables_2029():
    from src.leetcode_2029_stone_game_ix import Solution

    solution = Solution()

    def _init_variables_2029():
        return solution

    yield _init_variables_2029


class TestClass2029:
    def test_solution_0(self, init_variables_2029):
        assert init_variables_2029().stoneGameIX([2, 1])

    def test_solution_1(self, init_variables_2029):
        assert not init_variables_2029().stoneGameIX([2])

    def test_solution_2(self, init_variables_2029):
        assert not init_variables_2029().stoneGameIX([5, 1, 2, 4, 3])

    def test_solution_3(self, init_variables_2029):
        assert init_variables_2029().stoneGameIX([20, 3, 20, 17, 2, 12, 15, 17, 4])
