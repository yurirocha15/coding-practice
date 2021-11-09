#!/usr/bin/env python

import pytest

"""
Test 2048. Next Greater Numerically Balanced Number
"""


@pytest.fixture(scope="session")
def init_variables_2048():
    from src.leetcode_2048_next_greater_numerically_balanced_number import Solution

    solution = Solution()

    def _init_variables_2048():
        return solution

    yield _init_variables_2048


class TestClass2048:
    def test_solution_0(self, init_variables_2048):
        assert init_variables_2048().nextBeautifulNumber(1) == 22

    def test_solution_1(self, init_variables_2048):
        assert init_variables_2048().nextBeautifulNumber(1000) == 1333

    def test_solution_2(self, init_variables_2048):
        assert init_variables_2048().nextBeautifulNumber(3000) == 3133
