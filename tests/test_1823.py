#!/usr/bin/env python

import pytest

"""
Test 1823. Find the Winner of the Circular Game
"""


@pytest.fixture(scope="session")
def init_variables_1823():
    from src.leetcode_1823_find_the_winner_of_the_circular_game import Solution

    solution = Solution()

    def _init_variables_1823():
        return solution

    yield _init_variables_1823


class TestClass1823:
    def test_solution_0(self, init_variables_1823):
        assert init_variables_1823().findTheWinner(5, 2) == 3

    def test_solution_1(self, init_variables_1823):
        assert init_variables_1823().findTheWinner(6, 5) == 1
