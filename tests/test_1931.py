#!/usr/bin/env python

import pytest

"""
Test 1931. Painting a Grid With Three Different Colors
"""


@pytest.fixture(scope="session")
def init_variables_1931():
    from src.leetcode_1931_painting_a_grid_with_three_different_colors import Solution

    solution = Solution()

    def _init_variables_1931():
        return solution

    yield _init_variables_1931


class TestClass1931:
    def test_solution_0(self, init_variables_1931):
        assert init_variables_1931().colorTheGrid(1, 1) == 3

    def test_solution_1(self, init_variables_1931):
        assert init_variables_1931().colorTheGrid(1, 2) == 6

    def test_solution_2(self, init_variables_1931):
        assert init_variables_1931().colorTheGrid(5, 5) == 580986
