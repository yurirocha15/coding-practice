#!/usr/bin/env python

import pytest

"""
Test 2064. Minimized Maximum of Products Distributed to Any Store
"""


@pytest.fixture(scope="session")
def init_variables_2064():
    from src.leetcode_2064_minimized_maximum_of_products_distributed_to_any_store import Solution

    solution = Solution()

    def _init_variables_2064():
        return solution

    yield _init_variables_2064


class TestClass2064:
    def test_solution_0(self, init_variables_2064):
        assert init_variables_2064().minimizedMaximum(6, [11, 6]) == 3

    def test_solution_1(self, init_variables_2064):
        assert init_variables_2064().minimizedMaximum(7, [15, 10, 10]) == 5

    def test_solution_2(self, init_variables_2064):
        assert init_variables_2064().minimizedMaximum(1, [100000]) == 100000
