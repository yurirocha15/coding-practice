#!/usr/bin/env python

import pytest

"""
Test 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
"""


@pytest.fixture(scope="session")
def init_variables_1689():
    from src.leetcode_1689_partitioning_into_minimum_number_of_deci_binary_numbers import Solution

    solution = Solution()

    def _init_variables_1689():
        return solution

    yield _init_variables_1689


class TestClass1689:
    def test_solution_0(self, init_variables_1689):
        assert init_variables_1689().minPartitions("32") == 3

    def test_solution_1(self, init_variables_1689):
        assert init_variables_1689().minPartitions("82734") == 8

    def test_solution_2(self, init_variables_1689):
        assert init_variables_1689().minPartitions("27346209830709182346") == 9
