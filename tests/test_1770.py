#!/usr/bin/env python

import pytest

"""
Test 1770. Maximum Score from Performing Multiplication Operations
"""


@pytest.fixture(scope="session")
def init_variables_1770():
    from src.leetcode_1770_maximum_score_from_performing_multiplication_operations import Solution

    solution = Solution()

    def _init_variables_1770():
        return solution

    yield _init_variables_1770


class TestClass1770:
    def test_solution_0(self, init_variables_1770):
        assert init_variables_1770().maximumScore([1, 2, 3], [3, 2, 1]) == 14

    def test_solution_1(self, init_variables_1770):
        assert (
            init_variables_1770().maximumScore(
                [-5, -3, -3, -2, 7, 1], [-10, -5, 3, 4, 6]
            )
            == 102
        )
