#!/usr/bin/env python

import pytest

"""
Test 2032. Two Out of Three
"""


@pytest.fixture(scope="session")
def init_variables_2032():
    from src.leetcode_2032_two_out_of_three import Solution

    solution = Solution()

    def _init_variables_2032():
        return solution

    yield _init_variables_2032


class TestClass2032:
    def test_solution_0(self, init_variables_2032):
        assert init_variables_2032().twoOutOfThree([1, 1, 3, 2], [2, 3], [3]) in (
            [3, 2],
            [2, 3],
        )

    def test_solution_1(self, init_variables_2032):
        assert init_variables_2032().twoOutOfThree([3, 1], [2, 3], [1, 2]) in (
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        )

    def test_solution_2(self, init_variables_2032):
        assert init_variables_2032().twoOutOfThree([1, 2, 2], [4, 3, 3], [5]) == []
