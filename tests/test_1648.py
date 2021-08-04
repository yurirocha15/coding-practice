#!/usr/bin/env python

import pytest

"""
Test 1648. Sell Diminishing-Valued Colored Balls
"""


@pytest.fixture(scope="session")
def init_variables_1648():
    from src.leetcode_1648_sell_diminishing_valued_colored_balls import Solution

    solution = Solution()

    def _init_variables_1648():
        return solution

    yield _init_variables_1648


class TestClass1648:
    def test_solution_0(self, init_variables_1648):
        assert init_variables_1648().maxProfit([2, 5], 4) == 14

    def test_solution_1(self, init_variables_1648):
        assert init_variables_1648().maxProfit([3, 5], 6) == 19

    def test_solution_2(self, init_variables_1648):
        assert init_variables_1648().maxProfit([2, 8, 4, 10, 6], 20) == 110

    def test_solution_3(self, init_variables_1648):
        assert init_variables_1648().maxProfit([1000000000], 1000000000) == 21
