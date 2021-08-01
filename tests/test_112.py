#!/usr/bin/env python

import pytest

"""
Test 112. Path Sum
"""


@pytest.fixture(scope="session")
def init_variables_112():
    from src.leetcode_112_path_sum import Solution

    solution = Solution()

    def _init_variables_112():
        return solution

    yield _init_variables_112


class TestClass112:
    def test_solution_0(self, init_variables_112):
        assert init_variables_112().hasPathSum(
            [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22
        )

    def test_solution_1(self, init_variables_112):
        assert not init_variables_112().hasPathSum([1, 2, 3], 5)

    def test_solution_2(self, init_variables_112):
        assert not init_variables_112().hasPathSum([1, 2], 0)
