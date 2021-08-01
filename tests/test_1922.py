#!/usr/bin/env python

import pytest

"""
Test 1922. Count Good Numbers
"""


@pytest.fixture(scope="session")
def init_variables_1922():
    from src.leetcode_1922_count_good_numbers import Solution

    solution = Solution()

    def _init_variables_1922():
        return solution

    yield _init_variables_1922


class TestClass1922:
    def test_solution_0(self, init_variables_1922):
        assert init_variables_1922().countGoodNumbers(1) == 5

    def test_solution_1(self, init_variables_1922):
        assert init_variables_1922().countGoodNumbers(4) == 400

    def test_solution_2(self, init_variables_1922):
        assert init_variables_1922().countGoodNumbers(50) == 564908303
