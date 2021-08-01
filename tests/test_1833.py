#!/usr/bin/env python

import pytest

"""
Test 1833. Maximum Ice Cream Bars
"""


@pytest.fixture(scope="session")
def init_variables_1833():
    from src.leetcode_1833_maximum_ice_cream_bars import Solution

    solution = Solution()

    def _init_variables_1833():
        return solution

    yield _init_variables_1833


class TestClass1833:
    def test_solution_0(self, init_variables_1833):
        assert init_variables_1833().maxIceCream([1, 3, 2, 4, 1], 7) == 4

    def test_solution_1(self, init_variables_1833):
        assert init_variables_1833().maxIceCream([10, 6, 8, 7, 7, 8], 5) == 0

    def test_solution_2(self, init_variables_1833):
        assert init_variables_1833().maxIceCream([1, 6, 3, 1, 2, 5], 20) == 6
