#!/usr/bin/env python

import pytest

"""
Test 1793. Maximum Score of a Good Subarray
"""


@pytest.fixture(scope="session")
def init_variables_1793():
    from src.leetcode_1793_maximum_score_of_a_good_subarray import Solution

    solution = Solution()

    def _init_variables_1793():
        return solution

    yield _init_variables_1793


class TestClass1793:
    def test_solution_0(self, init_variables_1793):
        assert init_variables_1793().maximumScore([1, 4, 3, 7, 4, 5], 3) == 15

    def test_solution_1(self, init_variables_1793):
        assert init_variables_1793().maximumScore([5, 5, 4, 5, 4, 1, 1, 1], 0) == 20
