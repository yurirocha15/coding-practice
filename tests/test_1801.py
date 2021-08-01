#!/usr/bin/env python

import pytest

"""
Test 1801. Number of Orders in the Backlog
"""


@pytest.fixture(scope="session")
def init_variables_1801():
    from src.leetcode_1801_number_of_orders_in_the_backlog import Solution

    solution = Solution()

    def _init_variables_1801():
        return solution

    yield _init_variables_1801


class TestClass1801:
    def test_solution_0(self, init_variables_1801):
        assert (
            init_variables_1801().getNumberOfBacklogOrders(
                [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
            )
            == 6
        )

    def test_solution_1(self, init_variables_1801):
        assert (
            init_variables_1801().getNumberOfBacklogOrders(
                [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]
            )
            == 999999984
        )
