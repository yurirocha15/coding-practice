#!/usr/bin/env python

import pytest

"""
Test 1672. Richest Customer Wealth
"""


@pytest.fixture(scope="session")
def init_variables_1672():
    from src.leetcode_1672_richest_customer_wealth import Solution

    solution = Solution()

    def _init_variables_1672():
        return solution

    yield _init_variables_1672


class TestClass1672:
    def test_solution_0(self, init_variables_1672):
        assert init_variables_1672().maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6

    def test_solution_1(self, init_variables_1672):
        assert init_variables_1672().maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10

    def test_solution_2(self, init_variables_1672):
        assert (
            init_variables_1672().maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
        )
