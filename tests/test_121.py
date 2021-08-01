#!/usr/bin/env python

import pytest

"""
Test 121. Best Time to Buy and Sell Stock
"""


@pytest.fixture(scope="session")
def init_variables_121():
    from src.leetcode_121_best_time_to_buy_and_sell_stock import Solution

    solution = Solution()

    def _init_variables_121():
        return solution

    yield _init_variables_121


class TestClass121:
    def test_solution_0(self, init_variables_121):
        assert init_variables_121().maxProfit([7, 1, 5, 3, 6, 4]) == 5

    def test_solution_1(self, init_variables_121):
        assert init_variables_121().maxProfit([7, 6, 4, 3, 1]) == 0
