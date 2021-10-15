#!/usr/bin/env python

import pytest

"""
Test 2028. Find Missing Observations
"""


@pytest.fixture(scope="session")
def init_variables_2028():
    from src.leetcode_2028_find_missing_observations import Solution

    solution = Solution()

    def _init_variables_2028():
        return solution

    yield _init_variables_2028


class TestClass2028:
    def test_solution_0(self, init_variables_2028):
        assert init_variables_2028().missingRolls([3, 2, 4, 3], 4, 2) == [6, 6]

    def test_solution_1(self, init_variables_2028):
        assert init_variables_2028().missingRolls([1, 5, 6], 3, 4) == [2, 3, 2, 2]

    def test_solution_2(self, init_variables_2028):
        assert init_variables_2028().missingRolls([1, 2, 3, 4], 6, 4) == []

    def test_solution_3(self, init_variables_2028):
        assert init_variables_2028().missingRolls([1], 3, 1) == [5]
