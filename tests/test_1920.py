#!/usr/bin/env python

import pytest

"""
Test 1920. Build Array from Permutation
"""


@pytest.fixture(scope="session")
def init_variables_1920():
    from src.leetcode_1920_build_array_from_permutation import Solution

    solution = Solution()

    def _init_variables_1920():
        return solution

    yield _init_variables_1920


class TestClass1920:
    def test_solution_0(self, init_variables_1920):
        assert init_variables_1920().buildArray([0, 2, 1, 5, 3, 4]) == [
            0,
            1,
            2,
            4,
            5,
            3,
        ]

    def test_solution_1(self, init_variables_1920):
        assert init_variables_1920().buildArray([5, 0, 1, 2, 3, 4]) == [
            4,
            5,
            0,
            1,
            2,
            3,
        ]
