#!/usr/bin/env python

import pytest

"""
Test 2079. Watering Plants
"""


@pytest.fixture(scope="session")
def init_variables_2079():
    from src.leetcode_2079_watering_plants import Solution

    solution = Solution()

    def _init_variables_2079():
        return solution

    yield _init_variables_2079


class TestClass2079:
    def test_solution_0(self, init_variables_2079):
        assert init_variables_2079().wateringPlants([2, 2, 3, 3], 5) == 14

    def test_solution_1(self, init_variables_2079):
        assert init_variables_2079().wateringPlants([1, 1, 1, 4, 2, 3], 4) == 30

    def test_solution_2(self, init_variables_2079):
        assert init_variables_2079().wateringPlants([7, 7, 7, 7, 7, 7, 7], 8) == 49
