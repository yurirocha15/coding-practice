#!/usr/bin/env python

import pytest

"""
Test 1690. Stone Game VII
"""


@pytest.fixture(scope="session")
def init_variables_1690():
    from src.leetcode_1690_stone_game_vii import Solution

    solution = Solution()

    def _init_variables_1690():
        return solution

    yield _init_variables_1690


class TestClass1690:
    def test_solution_0(self, init_variables_1690):
        assert init_variables_1690().stoneGameVII([5, 3, 1, 4, 2]) == 6

    def test_solution_1(self, init_variables_1690):
        assert init_variables_1690().stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]) == 122
