#!/usr/bin/env python

import pytest

"""
Test 2078. Two Furthest Houses With Different Colors
"""


@pytest.fixture(scope="session")
def init_variables_2078():
    from src.leetcode_2078_two_furthest_houses_with_different_colors import Solution

    solution = Solution()

    def _init_variables_2078():
        return solution

    yield _init_variables_2078


class TestClass2078:
    def test_solution_0(self, init_variables_2078):
        assert init_variables_2078().maxDistance([1, 1, 1, 6, 1, 1, 1]) == 3

    def test_solution_1(self, init_variables_2078):
        assert init_variables_2078().maxDistance([1, 8, 3, 8, 3]) == 4

    def test_solution_2(self, init_variables_2078):
        assert init_variables_2078().maxDistance([0, 1]) == 1
