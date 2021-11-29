#!/usr/bin/env python

import pytest

"""
Test 2073. Time Needed to Buy Tickets
"""


@pytest.fixture(scope="session")
def init_variables_2073():
    from src.leetcode_2073_time_needed_to_buy_tickets import Solution

    solution = Solution()

    def _init_variables_2073():
        return solution

    yield _init_variables_2073


class TestClass2073:
    def test_solution_0(self, init_variables_2073):
        assert init_variables_2073().timeRequiredToBuy([2, 3, 2], 2) == 6

    def test_solution_1(self, init_variables_2073):
        assert init_variables_2073().timeRequiredToBuy([5, 1, 1, 1], 0) == 8
