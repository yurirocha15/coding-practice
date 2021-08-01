#!/usr/bin/env python

import pytest

"""
Test 1. Two Sum
"""


@pytest.fixture(scope="session")
def init_variables_1():
    from src.leetcode_1_two_sum import Solution

    solution = Solution()

    def _init_variables_1():
        return solution

    yield _init_variables_1


class TestClass1:
    def test_solution_0(self, init_variables_1):
        assert init_variables_1().twoSum([2, 7, 11, 15], 9) == [0, 1]

    def test_solution_1(self, init_variables_1):
        assert init_variables_1().twoSum([3, 2, 4], 6) == [1, 2]

    def test_solution_2(self, init_variables_1):
        assert init_variables_1().twoSum([3, 3], 6) == [0, 1]
