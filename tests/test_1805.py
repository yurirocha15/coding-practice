#!/usr/bin/env python

import pytest

"""
Test 1805. Number of Different Integers in a String
"""


@pytest.fixture(scope="session")
def init_variables_1805():
    from src.leetcode_1805_number_of_different_integers_in_a_string import Solution

    solution = Solution()

    def _init_variables_1805():
        return solution

    yield _init_variables_1805


class TestClass1805:
    def test_solution_0(self, init_variables_1805):
        assert init_variables_1805().numDifferentIntegers("a123bc34d8ef34") == 3

    def test_solution_1(self, init_variables_1805):
        assert init_variables_1805().numDifferentIntegers("leet1234code234") == 2

    def test_solution_2(self, init_variables_1805):
        assert init_variables_1805().numDifferentIntegers("a1b01c001") == 1
