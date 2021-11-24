#!/usr/bin/env python

import pytest

"""
Test 264. Ugly Number II
"""


@pytest.fixture(scope="session")
def init_variables_264():
    from src.leetcode_264_ugly_number_ii import Solution

    solution = Solution()

    def _init_variables_264():
        return solution

    yield _init_variables_264


class TestClass264:
    def test_solution_0(self, init_variables_264):
        assert init_variables_264().nthUglyNumber(10) == 12

    def test_solution_1(self, init_variables_264):
        assert init_variables_264().nthUglyNumber(1) == 1
