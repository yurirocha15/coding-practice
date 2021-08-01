#!/usr/bin/env python

import pytest

"""
Test 1840. Maximum Building Height
"""


@pytest.fixture(scope="session")
def init_variables_1840():
    from src.leetcode_1840_maximum_building_height import Solution

    solution = Solution()

    def _init_variables_1840():
        return solution

    yield _init_variables_1840


class TestClass1840:
    def test_solution_0(self, init_variables_1840):
        assert init_variables_1840().maxBuilding(5, [[2, 1], [4, 1]]) == 2

    def test_solution_1(self, init_variables_1840):
        assert init_variables_1840().maxBuilding(6, []) == 5

    def test_solution_2(self, init_variables_1840):
        assert (
            init_variables_1840().maxBuilding(10, [[5, 3], [2, 5], [7, 4], [10, 3]])
            == 5
        )
