#!/usr/bin/env python

import pytest

"""
Test 1856. Maximum Subarray Min-Product
"""


@pytest.fixture(scope="session")
def init_variables_1856():
    from src.leetcode_1856_maximum_subarray_min_product import Solution

    solution = Solution()

    def _init_variables_1856():
        return solution

    yield _init_variables_1856


class TestClass1856:
    def test_solution_0(self, init_variables_1856):
        assert init_variables_1856().maxSumMinProduct([1, 2, 3, 2]) == 14

    def test_solution_1(self, init_variables_1856):
        assert init_variables_1856().maxSumMinProduct([2, 3, 3, 1, 2]) == 18

    def test_solution_2(self, init_variables_1856):
        assert init_variables_1856().maxSumMinProduct([3, 1, 5, 6, 4, 2]) == 60
