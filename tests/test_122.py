#!/usr/bin/env python

import pytest

"""
Test 122. Best Time to Buy and Sell Stock II
"""


@pytest.fixture(scope="session")
def init_variables_122():
    from src.leetcode_122_best_time_to_buy_and_sell_stock_ii import Solution

    solution = Solution()

    def _init_variables_122():
        return solution

    yield _init_variables_122


class TestClass122:
    def test_solution_0(self, init_variables_122):
        assert init_variables_122().maxProfit([7, 1, 5, 3, 6, 4]) == 7

    def test_solution_1(self, init_variables_122):
        assert init_variables_122().maxProfit([1, 2, 3, 4, 5]) == 4

    def test_solution_2(self, init_variables_122):
        assert init_variables_122().maxProfit([7, 6, 4, 3, 1]) == 0
