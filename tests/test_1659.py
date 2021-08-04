#!/usr/bin/env python

import pytest

"""
Test 1659. Maximize Grid Happiness
"""


@pytest.fixture(scope="session")
def init_variables_1659():
    from src.leetcode_1659_maximize_grid_happiness import Solution

    solution = Solution()

    def _init_variables_1659():
        return solution

    yield _init_variables_1659


class TestClass1659:
    def test_solution_0(self, init_variables_1659):
        assert init_variables_1659().getMaxGridHappiness(2, 3, 1, 2) == 240

    def test_solution_1(self, init_variables_1659):
        assert init_variables_1659().getMaxGridHappiness(3, 1, 2, 1) == 260

    def test_solution_2(self, init_variables_1659):
        assert init_variables_1659().getMaxGridHappiness(2, 2, 4, 0) == 240
