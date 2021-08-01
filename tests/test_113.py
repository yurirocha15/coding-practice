#!/usr/bin/env python

import pytest

"""
Test 113. Path Sum II
"""


@pytest.fixture(scope="session")
def init_variables_113():
    from src.leetcode_113_path_sum_ii import Solution

    solution = Solution()

    def _init_variables_113():
        return solution

    yield _init_variables_113


class TestClass113:
    def test_solution_0(self, init_variables_113):
        assert init_variables_113().pathSum(
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22
        ) == [[5, 4, 11, 2], [5, 8, 4, 5]]

    def test_solution_1(self, init_variables_113):
        assert init_variables_113().pathSum([1, 2, 3], 5) == []

    def test_solution_2(self, init_variables_113):
        assert init_variables_113().pathSum([1, 2], 0) == []
