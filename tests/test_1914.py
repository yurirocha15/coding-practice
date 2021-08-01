#!/usr/bin/env python

import pytest

"""
Test 1914. Cyclically Rotating a Grid
"""


@pytest.fixture(scope="session")
def init_variables_1914():
    from src.leetcode_1914_cyclically_rotating_a_grid import Solution

    solution = Solution()

    def _init_variables_1914():
        return solution

    yield _init_variables_1914


class TestClass1914:
    def test_solution_0(self, init_variables_1914):
        assert init_variables_1914().rotateGrid([[40, 10], [30, 20]], 1) == [
            [10, 20],
            [40, 30],
        ]

    def test_solution_1(self, init_variables_1914):
        assert init_variables_1914().rotateGrid(
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 2
        ) == [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 9, 13, 14]]
